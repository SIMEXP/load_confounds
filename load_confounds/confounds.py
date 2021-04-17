"""Helper functions for the manipulation of confounds.

Authors: load_confounds team
"""
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import warnings
import os
import json
import glob
import re


img_file_patern = "_space-*_bold.*nii*"
aroma_keword = "_desc-smoothAROMAnonaggr_bold"

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


def _sanitize_confounds(confounds_raw):
    """Make sure the inputs are in the correct format."""
    # we want to support loading a single set of confounds, instead of a list
    # so we hack it
    flag_single = isinstance(confounds_raw, str) or isinstance(
        confounds_raw, pd.DataFrame
    )
    if flag_single:
        confounds_raw = [confounds_raw]

    return confounds_raw, flag_single


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
    suffix = "_space-" + nii_file.split("space-")[1]
    # fmriprep has changed the file suffix between v20.1.1 and v20.2.0 with respect to BEP 012.
    # cf. https://neurostars.org/t/naming-change-confounds-regressors-to-confounds-timeseries/17637
    # Check file with new naming scheme exists or replace, for backward compatibility.
    confounds_raw_candidates = [
        nii_file.replace(suffix, "_desc-confounds_timeseries.tsv",),
        nii_file.replace(suffix, "_desc-confounds_regressors.tsv",)
        ]

    confounds_raw = []
    for cr in confounds_raw_candidates:
        if os.path.exists(cr):
            confounds_raw.append(cr)
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


def _check_images(nii_file, flag_full_aroma):
    """Validate input nifti/cifti files and ICA AROMA related files"""
    aroma_relevant = (aroma_keword in nii_file)
    if flag_full_aroma and not aroma_relevant:
        raise ValueError(f"Input must be ~desc-smoothAROMAnonaggr_bold for ICA-AROMA based strategy.")
    valid_nii = re.search("_bold.*.nii.*", nii_file)
    if not valid_nii:
        raise ValueError(f"Input {nii_file} is not a fMRIprep processed functional image file.")


def _confounds_to_df(nii_file, flag_acompcor, flag_full_aroma):
    """Load raw confounds as a pandas DataFrame."""
    _check_images(nii_file, flag_full_aroma)
    confounds_raw = _get_file_raw(nii_file)
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
