"""Helper functions for the manipulation of confounds.

Authors: load_confounds team
"""
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import os
import json
import re


img_file_patterns = {
    "aroma": "_desc-smoothAROMAnonaggr_bold",
    "nii.gz": "_space-.*_desc-preproc_bold.nii.gz",
    "dtseries.nii": "_space-.*_bold.dtseries.nii",
    "func.gii": "_space-.*_hemi-[LR]_bold.func.gii",
}

img_file_error = {
    "aroma": "Input must be ~desc-smoothAROMAnonaggr_bold for full ICA-AROMA strategy.",
    "nii.gz": "Invalid file type for the selected method.",
    "dtseries.nii": "Invalid file type for the selected method.",
    "func.gii": "need fMRIprep output with extension func.gii",
}


def _check_params(confounds_raw, params):
    """Check that specified parameters can be found in the confounds."""
    not_found_params = []
    for par in params:
        if not par in confounds_raw.columns:
            not_found_params.append(par)
    if not_found_params:
        raise MissingConfound(params=not_found_params)
    return None


def _find_confounds(confounds_raw, keywords):
    """Find confounds that contain certain keywords."""
    list_confounds = []
    missing_keys = []
    for key in keywords:
        key_found = [col for col in confounds_raw.columns if key in col]
        if not key_found:
            missing_keys.append(key)
        else:
            list_confounds.extend(key_found)
    if missing_keys:
        raise MissingConfound(keywords=missing_keys)
    return list_confounds


def _flag_single_gifti(img_files):
    """Test if the paired input files are giftis."""
    flag_single_gifti = []  # gifti in pairs
    for img in img_files:
        ext = ".".join(img.split(".")[-2:])
        flag_single_gifti.append((ext == "func.gii"))
    return all(flag_single_gifti)


def _sanitize_confounds(img_files):
    """Make sure the inputs are in the correct format."""
    # we want to support loading a single set of confounds, instead of a list
    # so we hack it
    if isinstance(img_files, list) and len(img_files) == 2:
        flag_single = _flag_single_gifti(img_files)
    else:  # single file
        flag_single = isinstance(img_files, str)

    if flag_single:
        img_files = [img_files]
    return img_files, flag_single


def _add_suffix(params, model):
    """
    Add suffixes to a list of parameters.
    Suffixes includes derivatives, power2 and full
    """
    params_full = params.copy()
    suffix = {
        "basic": {},
        "derivatives": {"derivative1"},
        "power2": {"power2"},
        "full": {"derivative1", "power2", "derivative1_power2"},
    }
    for par in params:
        for suff in suffix[model]:
            params_full.append(f"{par}_{suff}")
    return params_full


def _pca_motion(confounds_motion, n_components):
    """Reduce the motion paramaters using PCA."""
    n_available = confounds_motion.shape[1]
    if n_components > n_available:
        raise ValueError(
            f"User requested n_motion={n_components} motion components, but found only {n_available}."
        )
    confounds_motion = confounds_motion.dropna()
    confounds_motion_std = scale(
        confounds_motion, axis=0, with_mean=True, with_std=True
    )
    pca = PCA(n_components=n_components)
    motion_pca = pd.DataFrame(pca.fit_transform(confounds_motion_std))
    motion_pca.columns = ["motion_pca_" + str(col + 1) for col in motion_pca.columns]
    return motion_pca


def _optimize_scrub(fd_outliers, n_scans):
    """
    Perform optimized scrub. After scrub volumes, further remove
    continuous segments containing fewer than 5 volumes.
    Power, Jonathan D., et al. "Methods to detect, characterize, and remove
    motion artifact in resting state fMRI." Neuroimage 84 (2014): 320-341.
    """
    # Start by checking if the beginning continuous segment is fewer than 5 volumes
    if fd_outliers[0] < 5:
        fd_outliers = np.asarray(list(range(fd_outliers[0])) + list(fd_outliers))
    # Do the same for the ending segment of scans
    if n_scans - (fd_outliers[-1] + 1) < 5:
        fd_outliers = np.asarray(
            list(fd_outliers) + list(range(fd_outliers[-1], n_scans))
        )
    # Now do everything in between
    fd_outlier_ind_diffs = np.diff(fd_outliers)
    short_segments_inds = np.where(
        np.logical_and(fd_outlier_ind_diffs > 1, fd_outlier_ind_diffs < 6)
    )[0]
    for ind in short_segments_inds:
        fd_outliers = np.asarray(
            list(fd_outliers) + list(range(fd_outliers[ind] + 1, fd_outliers[ind + 1]))
        )
    fd_outliers = np.sort(np.unique(fd_outliers))
    return fd_outliers


def _get_file_raw(nii_file):
    """Get the name of the raw confound file."""
    if isinstance(nii_file, list):  # catch gifti
        nii_file = nii_file[0]
    suffix = "_space-" + nii_file.split("space-")[1]
    # fmriprep has changed the file suffix between v20.1.1 and v20.2.0 with respect to BEP 012.
    # cf. https://neurostars.org/t/naming-change-confounds-regressors-to-confounds-timeseries/17637
    # Check file with new naming scheme exists or replace, for backward compatibility.
    confounds_raw_candidates = [
        nii_file.replace(
            suffix,
            "_desc-confounds_timeseries.tsv",
        ),
        nii_file.replace(
            suffix,
            "_desc-confounds_regressors.tsv",
        ),
    ]

    confounds_raw = [cr for cr in confounds_raw_candidates if os.path.exists(cr)]

    if not confounds_raw:
        raise ValueError("Could not find associated confound file.")
    elif len(confounds_raw) != 1:
        raise ValueError("Found more than one confound file.")
    else:
        return confounds_raw[0]


def _get_json(confounds_raw, flag_acompcor):
    """Load json data companion to the confounds tsv file."""
    # Load JSON file
    confounds_json = confounds_raw.replace("tsv", "json")
    try:
        with open(confounds_json, "rb") as f:
            confounds_json = json.load(f)
    except OSError:
        if flag_acompcor:
            raise ValueError(
                f"Could not find a json file {confounds_json}. This is necessary for anat compcor"
            )
    return confounds_json


def _ext_validator(image_file, ext):
    """Check image is valid based on extention."""
    try:
        valid_img = all(
            bool(re.search(img_file_patterns[ext], img)) for img in image_file
        )
        error_message = img_file_error[ext]
    except KeyError:
        valid_img = False
        error_message = "Unsupported input."
    return valid_img, error_message


def _check_images(image_file, flag_full_aroma):
    """Validate input file and ICA AROMA related file."""
    if len(image_file) == 2:  # must be gifti
        valid_img, error_message = _ext_validator(image_file, "func.gii")
    elif flag_full_aroma:
        valid_img, error_message = _ext_validator([image_file], "aroma")
    else:
        ext = ".".join(image_file.split(".")[-2:])
        valid_img, error_message = _ext_validator([image_file], ext)
    if not valid_img:
        raise ValueError(error_message)


def _confounds_to_df(image_file, flag_acompcor, flag_full_aroma):
    """Load raw confounds as a pandas DataFrame."""
    _check_images(image_file, flag_full_aroma)
    confounds_raw = _get_file_raw(image_file)
    confounds_json = _get_json(confounds_raw, flag_acompcor)
    confounds_raw = pd.read_csv(confounds_raw, delimiter="\t", encoding="utf-8")
    return confounds_raw, confounds_json


def _confounds_to_ndarray(confounds, demean):
    """Convert confounds from a pandas dataframe to a numpy array."""
    # Convert from DataFrame to numpy ndarray
    labels = confounds.columns
    confounds = confounds.values

    # Derivatives have NaN on the first row
    # Replace them by estimates at second time point,
    # otherwise nilearn will crash.
    if confounds.size != 0:  # ica_aroma = "full" generate empty output
        mask_nan = np.isnan(confounds[0, :])
        confounds[0, mask_nan] = confounds[1, mask_nan]

        # Optionally demean confounds
        if demean:
            confounds = scale(confounds, axis=0, with_std=False)

    return confounds, labels


class MissingConfound(Exception):
    """
    Exception raised when failing to find params in the confounds.

    Parameters
    ----------
        params : list of missing params
        keywords: list of missing keywords
    """

    def __init__(self, params=None, keywords=None):
        """Default values are empty lists."""
        self.params = params if params else []
        self.keywords = keywords if keywords else []
