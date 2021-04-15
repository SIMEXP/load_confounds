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


prefix_compcor = {"full": ["t", "a"],
                   "temp": ["t"],
                   "anat": ["a"]}
anat_masker = {True: ["combined"], False: ["WM", "CSF"], None: None}


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
        key_found = False
        for col in confounds_raw.columns:
            if key in col:
                list_confounds.append(col)
                key_found = True
        if not key_found:
            missing_keys.append(key)
    if missing_keys:
        raise MissingConfound(keywords=missing_keys)
    return list_confounds


def _select_compcor(compcor_cols, n_compcor):
    """Retain a specified number of compcor components."""
    # only select if not "auto", or less components are requested than there actually is
    if (n_compcor != "auto") and (n_compcor < len(compcor_cols)):
        compcor_cols = compcor_cols[0:n_compcor]
    return compcor_cols


def _check_compcor_method(compcor, acompcor_combined):
    """load compcor options and check if method is acceptable"""
    # get relevant prefix from compcor strategy
    prefix_set = prefix_compcor[compcor]
    # get relevant compcore mask
    anat_mask = anat_masker[acompcor_combined]
    if ("a" in prefix_set) and (anat_mask is None):
        raise ValueError(f"acompcor_combined must set to True or False. Got {acompcor_combined}")
    return prefix_set, anat_mask


def _find_compcor(confounds_json, compcor, n_compcor, acompcor_combined):
    """Builds list for the number of compcor components."""
    prefix_set, anat_mask = _check_compcor_method(compcor, acompcor_combined)

    collector = []
    for prefix in prefix_set:
        # all possible compcor confounds, mixing different types of mask
        all_compcor_name = [
            comp for comp in confounds_json.keys() if f"{prefix}_comp_cor" in comp
        ]
        # filter by prefix first and apply acompor mask option if relevant
        compcor_cols_filt = _prefix_confound_filter(prefix, all_compcor_name)
        if prefix == "a":
            compcor_cols_filt = _acompcor_mask(confounds_json, anat_mask, compcor_cols_filt)
        collector += compcor_cols_filt
    return _select_compcor(collector, n_compcor)


def _acompcor_mask(confounds_json, anat_mask, compcor_cols_filt):
    """filter according to acompcor mask"""
    cols = []
    for compcor_col in compcor_cols_filt:
        if confounds_json[compcor_col]["Mask"] in anat_mask:
            cols.append(compcor_col)
    return cols


def _prefix_confound_filter(prefix, all_compcor_name):
    """get confound columns by prefix and acompcor mask"""
    compcor_cols_filt = []
    for nn in range(len(all_compcor_name)):
        nn_str = str(nn).zfill(2)
        compcor_col = f"{prefix}_comp_cor_{nn_str}"
        compcor_cols_filt.append(compcor_col)
    return compcor_cols_filt



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


def _get_file_raw(confounds_raw):
    """Get the name of the raw confound file."""
    if "nii" in confounds_raw[-6:]:
        suffix = "_space-" + confounds_raw.split("space-")[1]
        confounds_raw = confounds_raw.replace(suffix, "_desc-confounds_timeseries.tsv",)
        # fmriprep has changed the file suffix between v20.1.1 and v20.2.0 with respect to BEP 012.
        # cf. https://neurostars.org/t/naming-change-confounds-regressors-to-confounds-timeseries/17637
        # Check file with new naming scheme exists or replace, for backward compatibility.
        if not os.path.exists(confounds_raw):
            confounds_raw = confounds_raw.replace(
                "_desc-confounds_timeseries.tsv", "_desc-confounds_regressors.tsv",
            )
    return confounds_raw


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


def _confounds_to_df(confounds_raw, flag_acompcor):
    """Load raw confounds as a pandas DataFrame."""
    confounds_raw = _get_file_raw(confounds_raw)
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
