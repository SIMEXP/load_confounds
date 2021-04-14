"""Predefined denoising strategies.

Authors: load_confounds team
"""
from .parser import Confounds


class Params2(Confounds):
    """
    Load confounds using the 2P strategy from Ciric et al. 2017.
    Mean white matter and CSF signals, with high-pass filter.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "wm_csf"]
        self.wm_csf = "basic"
        self.demean = demean


class Params6(Confounds):
    """
    Load confounds using the 6P strategy from Ciric et al. 2017.
    Basic motion parameters with high pass filter.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion"]
        self.motion = "basic"
        self.n_motion = 0
        self.demean = demean


class Params9(Confounds):
    """
    Load confounds using the 9P strategy from Ciric et al. 2017.
    Basic motion parameters, WM/CSF signals, global signal and high pass filter.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "wm_csf", "global"]
        self.motion = "basic"
        self.n_motion = 0
        self.wm_csf = "basic"
        self.global_signal = "basic"
        self.demean = demean


class Params9Scrub(Confounds):
    """
    Load confounds using a variant of the 9P strategy from Ciric et al. 2017.
    Basic motion parameters, WM/CSF signals, scrubbbing (full) and high pass filter.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    fd_thresh : float, optional
        Framewise displacement threshold for scrub (default = 0.2 mm)

    std_dvars_thresh : float, optional
        Standardized DVARS threshold for scrub (default = 3)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, fd_thresh=0.2, std_dvars_thresh=3, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "wm_csf", "scrub"]
        self.motion = "basic"
        self.n_motion = 0
        self.wm_csf = "basic"
        self.scrub = ("full",)
        self.fd_thresh = (fd_thresh,)
        self.std_dvars_thresh = (std_dvars_thresh,)
        self.demean = demean


class Params24(Confounds):
    """
    Load confounds using the 24P strategy from Ciric et al. 2017.
    Full motion parameters (derivatives, squares and squared derivatives),
    with high pass filter.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion"]
        self.motion = "full"
        self.n_motion = 0
        self.demean = demean


class Params36(Confounds):
    """
    Load confounds using the 36P strategy from Ciric et al. 2017.
    Motion parameters, WM/CSF signals, global signal, high pass filter.
    All noise components are fully expanded (derivatives, squares and squared
    derivatives).

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "wm_csf", "global"]
        self.motion = "full"
        self.n_motion = 0
        self.wm_csf = "full"
        self.global_signal = "full"
        self.demean = demean


class Params36Scrub(Confounds):
    """
    Load confounds using a variant of the 36P strategy from Ciric et al. 2017.
    Motion parameters, WM/CSF signals, scrub (full), high pass filter.
    All noise components are fully expanded (derivatives, squares and squared
    derivatives).

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    fd_thresh : float, optional
        Framewise displacement threshold for scrub (default = 0.2 mm)

    std_dvars_thresh : float, optional
        Standardized DVARS threshold for scrub (default = 3)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, fd_thresh=0.2, std_dvars_thresh=3, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "wm_csf", "scrub"]
        self.motion = "full"
        self.n_motion = 0
        self.wm_csf = "full"
        self.scrub = "full"
        self.fd_thresh = (fd_thresh,)
        self.std_dvars_thresh = (std_dvars_thresh,)
        self.demean = demean


class AnatCompCor(Confounds):
    """
    Load confounds using the aCOMPCOR strategy from Ciric et al. 2017.
    Motion parameters (fully expanded), high pass filter, and acompcor.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    n_compcor : int or "auto", optional
        The number of noise components to be extracted.
        Default is "auto": select all components (50% variance explained by fMRIPrep defaults)

    acompcor_combined: boolean, optional
        If true, use components generated from the combined white matter and csf
        masks. Otherwise, components are generated from each mask separately and then
        concatenated.

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, n_compcor="auto", demean=True, acompcor_combined=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "compcor"]
        self.motion = "full"
        self.n_motion = 0
        self.compcor = "anat"
        self.n_compcor = n_compcor
        self.acompcor_combined = acompcor_combined
        self.demean = demean


class TempCompCor(Confounds):
    """
    Load confounds using the tCOMPCOR strategy from Ciric et al. 2017.
    High pass filter, and tcompcor.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    n_compcor : int or "auto", optional
        The number of noise components to be extracted.
        Default is "auto": select all components (50% variance explained by fMRIPrep defaults)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, n_compcor="auto", demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "compcor"]
        self.compcor = "temp"
        self.n_compcor = n_compcor
        self.acompcor_combined = None
        self.demean = demean


class ICAAROMA(Confounds):
    """
    Load confounds for post-non-aggresive ICA-AROMA strategy described in Prium et al. 2015 and Ciric et al. 2017.
    The strategy requires fMRIprep output `*desc-smoothAROMAnonaggr_bold`.
    The generated confound regressors can only be used on `*desc-smoothAROMAnonaggr_bold`.

    ICA-AROMA steps in Ciric et al. 2017 are as followed:
    1. A non-aggressive de-noising immediately after ICA classification by partial regression.
    2. Confound regression step (mean signals from WM and CSF)

    In correspondent to fMRIprep and load_confounds:
    1. Denoising `*desc-smoothAROMAnonaggr_bold` generated by fMRIprep.
    2. Confound regressors generated by `load_confounds.ICAAROMA`

    In fMRIprep implementation, step 1  denoising is performed in `MNI152NLin6Asym` space only.
    To produce step 1 in other spacial template, one can use FSL function `fsl_regfilt`.
    For example, native T1w space:
    ```
    fsl_regfilt -i sub-<subject_label>_task-<task_id>_space-T1w_desc-preproc_bold.nii.gz \
        -f $(cat sub-<subject_label>_task-<task_id>_AROMAnoiseICs.csv) \
        -d sub-<subject_label>_task-<task_id>_desc-MELODIC_mixing.tsv \
        -o sub-<subject_label>_task-<task_id>_space-T1w_desc-AROMAnonaggr_bold.nii.gz
    ```

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    Notes
    -----
    fMRIprep documentation on ICA-AROMA
    https://fmriprep.org/en/latest/workflows.html?highlight=aggressive#ica-aroma

    For more discussion regarding the implementation in fMRIprep, please see notebook 5.
    https://github.com/nipreps/fmriprep-notebooks/

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["wm_csf", "high_pass"]
        self.demean = demean
        self.wm_csf = "basic"


class AROMAGSR(Confounds):
    """
    Load confounds for post-non-aggresive AROMA-GSR strategy from Ciric et al. 2017.
    The strategy requires fMRIprep output `*desc-smoothAROMAnonaggr_bold`.
    The generated confound regressors can only be used on `*desc-smoothAROMAnonaggr_bold`.
    In fMRIprep, ICA-AROMA denoising is performed in `MNI152NLin6Asym` space only.

    ICA-AROMA steps in Ciric et al. 2017 are as followed:
    1. A non-aggressive de-noising immediately after ICA classification by partial regression.
    2. Confound regression step. (mean signals from WM and CSF and global signal)

    In correspondent to fMRIprep and load_confounds:
    1. Denoising `*desc-smoothAROMAnonaggr_bold` generated by fMRIprep.
    2. Confound regressors generated by `load_confounds.AROMAGSR`

    In fMRIprep implementation, step 1  denoising is performed in `MNI152NLin6Asym` space only.
    To produce step 1 in other spacial template, one can use FSL function `fsl_regfilt`.
    For example, native T1w space:
    ```
    fsl_regfilt -i sub-<subject_label>_task-<task_id>_space-T1w_desc-preproc_bold.nii.gz \
        -f $(cat sub-<subject_label>_task-<task_id>_AROMAnoiseICs.csv) \
        -d sub-<subject_label>_task-<task_id>_desc-MELODIC_mixing.tsv \
        -o sub-<subject_label>_task-<task_id>_space-T1w_desc-AROMAnonaggr_bold.nii.gz
    ```
    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    Notes
    -----
    fMRIprep documentation on ICA-AROMA
    https://fmriprep.org/en/latest/workflows.html?highlight=aggressive#ica-aroma

    For more discussion regarding the implementation in fMRIprep, please see notebook 5.
    https://github.com/nipreps/fmriprep-notebooks/

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["wm_csf", "high_pass", "global"]
        self.global_signal = "basic"
        self.wm_csf = "basic"
        self.demean = demean


class AggrICAAROMA(Confounds):
    """
    Load confounds for aggresive ICA-AROMA strategy described in Prium et al. 2015.
    This strategy must be performed on output `*_desc-prepro_bold`.
    All variance associated with these noise ICs will be removed, including shared-variance with ‘good’ ICs.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    Notes
    -----
    fMRIprep documentation on ICA-AROMA
    https://fmriprep.org/en/latest/workflows.html?highlight=aggressive#ica-aroma

    For more discussion regarding the implementation in fMRIprep, please see notebook 5.
    https://github.com/nipreps/fmriprep-notebooks/

    """

    def __init__(self, demean=True):
        """Default parameters."""
        self.strategy = ["wm_csf", "high_pass", "global", "ica_aroma"]
        self.global_signal = "basic"
        self.wm_csf = "basic"
        self.demean = demean
