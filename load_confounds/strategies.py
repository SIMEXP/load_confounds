"""Predefined denoising strategies.

Authors: load_confounds team
"""
import warnings
from .parser import Confounds


class Minimal(Confounds):
    """
    Load confounds for a minimal denosing strategy commonly used
    in resting state functional connectivity, described in Fox et al., 2005.
    Full motion parameters, WM/CSF signals, and high pass filter,
    with an option to extract global signal confounds.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    motion : string, optional
        Type of confounds extracted from head motion estimates.
        "basic" translation/rotation (6 parameters)
        "power2" translation/rotation + quadratic terms (12 parameters)
        "derivatives" translation/rotation + derivatives (12 parameters)
        "full" translation/rotation + derivatives + quadratic terms + power2d derivatives (24 parameters)

    wm_csf : string, optional
        Type of confounds extracted from masks of white matter and cerebrospinal fluids.
        "basic" the averages in each mask (2 parameters)
        "power2" averages and quadratic terms (4 parameters)
        "derivatives" averages and derivatives (4 parameters)
        "full" averages + derivatives + quadratic terms + power2d derivatives (8 parameters)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    global_signal : string, optional
        Specify type of confounds extracted from the global signal.
        Global signal regressors will not be retrieved if no arguments were applied.
        "basic" just the global signal (1 parameter)
        "power2" global signal and quadratic term (2 parameters)
        "derivatives" global signal and derivative (2 parameters)
        "full" global signal + derivatives + quadratic terms + power2d derivatives (4 parameters)

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(self, motion="full", wm_csf="basic", demean=True, **kwargs):
        """Default parameters."""
        # check if global signal is supplied as a parameter
        # if so, add to strategy
        global_signal = kwargs.get("global_signal", False)
        strategy = ["high_pass", "motion", "wm_csf"]
        strategy, global_signal = _update_strategy(strategy, global_signal)
        # warn user for supplying useless parameter
        _check_invalid_parameter(kwargs, valid_keys=["global_signal"])

        # set attributes
        self.strategy = strategy
        self.motion = motion
        self.n_motion = 0
        self.wm_csf = wm_csf
        self.demean = demean
        if global_signal:
            self.global_signal = global_signal


class Scrubbing(Confounds):
    """
    Load confounds for scrubbing describbed in Power et al., 2012.
    Motion parameters, WM/CSF signals, scrub (full), high pass filter.
    All noise components are fully expanded (derivatives, squares and squared
    derivatives).

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    motion : string, optional
        Type of confounds extracted from head motion estimates.
        "basic" translation/rotation (6 parameters)
        "power2" translation/rotation + quadratic terms (12 parameters)
        "derivatives" translation/rotation + derivatives (12 parameters)
        "full" translation/rotation + derivatives + quadratic terms + power2d derivatives (24 parameters)

    wm_csf : string, optional
        Type of confounds extracted from masks of white matter and cerebrospinal fluids.
        "basic" the averages in each mask (2 parameters)
        "power2" averages and quadratic terms (4 parameters)
        "derivatives" averages and derivatives (4 parameters)
        "full" averages + derivatives + quadratic terms + power2d derivatives (8 parameters)

    scrub : string, optional
        Type of scrub of frames with excessive motion (Power et al. 2014)
        "basic" remove time frames based on excessive FD and DVARS
        "full" also remove time windows which are too short after scrubbing.
        one-hot encoding vectors are added as regressors for each scrubbed frame.

    fd_thresh : float, optional
        Framewise displacement threshold for scrub (default = 0.2 mm)

    std_dvars_thresh : float, optional
        Standardized DVARS threshold for scrub (default = 3)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    global_signal : string, optional
        Specify type of confounds extracted from the global signal.
        Global signal regressors will not be retrieved if no arguments were applied.
        "basic" just the global signal (1 parameter)
        "power2" global signal and quadratic term (2 parameters)
        "derivatives" global signal and derivative (2 parameters)
        "full" global signal + derivatives + quadratic terms + power2d derivatives (4 parameters)

    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    """

    def __init__(
        self,
        motion="full",
        wm_csf="full",
        scrub="full",
        fd_thresh=0.2,
        std_dvars_thresh=3,
        demean=True,
        **kwargs,
    ):
        """Default parameters."""
        # check if global signal is supplied as a parameter
        # if so, add to strategy
        global_signal = kwargs.get("global_signal", False)
        strategy = ["high_pass", "motion", "wm_csf", "scrub"]
        strategy, global_signal = _update_strategy(strategy, global_signal)
        # warn user for supplying useless parameter
        _check_invalid_parameter(kwargs, valid_keys=["global_signal"])

        # set attributes
        self.strategy = strategy
        self.motion = motion
        self.n_motion = 0
        self.wm_csf = wm_csf
        self.scrub = scrub
        self.fd_thresh = (fd_thresh,)
        self.std_dvars_thresh = (std_dvars_thresh,)
        self.demean = demean
        if global_signal:
            self.global_signal = global_signal


class CompCor(Confounds):
    """
    Load confounds using the CompCor strategy from Behzadi et al., 2007.
    Default with motion parameters (fully expanded), high pass filter, and anatomical compcor.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    motion : string, optional
        Type of confounds extracted from head motion estimates.
        "basic" translation/rotation (6 parameters)
        "power2" translation/rotation + quadratic terms (12 parameters)
        "derivatives" translation/rotation + derivatives (12 parameters)
        "full" translation/rotation + derivatives + quadratic terms + power2d derivatives (24 parameters)

    n_compcor : int or "auto", optional
        The number of noise components to be extracted. For acompcor_combined=False,
        this is the number of components per mask.
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

    def __init__(
        self,
        motion="full",
        compcor="anat",
        n_compcor="auto",
        demean=True,
        acompcor_combined=True,
    ):
        """Default parameters."""
        # set attributes
        self.strategy = ["high_pass", "motion", "compcor"]
        self.motion = motion
        self.n_motion = 0
        self.compcor = compcor
        self.n_compcor = n_compcor
        self.acompcor_combined = acompcor_combined
        self.demean = demean


class ICAAROMA(Confounds):
    """
    Load confounds for non-aggresive ICA-AROMA strategy from Pruim et al., 2015.
    The strategy requires fMRIprep outputs generated with `--use-aroma`.

    ICA-AROMA is implemented in two steps:
    1. A non-aggressive denoising immediately after ICA classification.
        A linear regression estimates signals with all independent components
        as predictors.
        A partial regression is then applied to remove variance associated
        with noise independent components.
        fMRIprep perfoms this step and generates files suffixed with
        `desc-smoothAROMAnonaggr_bold`.
    2. Confound regression step (mean signals from WM and CSF)
        Confound regressors generated by `load_confounds.ICAAROMA`.
        The generated confound regressors must only be used on fMRIprep output
        suffixed `desc-smoothAROMAnonaggr_bold`.

    `desc-smoothAROMAnonaggr_bold` is generated in `MNI152NLin6Asym` only.
    To produce `desc-smoothAROMAnonaggr_bold` in other spatial templates,
    use FSL function `fsl_regfilt`. For example, native T1w space:
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

    wm_csf : string, optional
        Type of confounds extracted from masks of white matter and cerebrospinal fluids.
        "basic" the averages in each mask (2 parameters)
        "power2" averages and quadratic terms (4 parameters)
        "derivatives" averages and derivatives (4 parameters)
        "full" averages + derivatives + quadratic terms + power2d derivatives (8 parameters)

    demean : boolean, optional
        If True, the confounds are standardized to a zero mean (over time).
        This step is critical if the confounds are regressed out of time series
        using nilearn with no or zscore standardization, but should be turned off
        with "spc" normalization.

    global_signal : string, optional
        Specify type of confounds extracted from the global signal.
        Global signal regressors will not be retrieved if no arguments were applied.
        "basic" just the global signal (1 parameter)
        "power2" global signal and quadratic term (2 parameters)
        "derivatives" global signal and derivative (2 parameters)
        "full" global signal + derivatives + quadratic terms + power2d derivatives (4 parameters)


    Returns
    -------
    conf :  a Confounds object
        conf.confounds_ is a reduced version of fMRIprep confounds.

    Notes
    -----
    fMRIprep documentation on ICA-AROMA
    https://fmriprep.org/en/latest/workflows.html#ica-aroma

    For more discussion regarding choosing the nuisance regressors before or
    after denoising with ICA-AROMA has a detriment on outcome measures,
    please see notebook 5.
    https://github.com/nipreps/fmriprep-notebooks/

    """

    def __init__(self, wm_csf="basic", demean=True, **kwargs):
        """Default parameters."""
        strategy = ["wm_csf", "high_pass", "ica_aroma"]
        global_signal = kwargs.get("global_signal", False)
        strategy, global_signal = _update_strategy(strategy, global_signal)
        # warn user for supplying useless parameter
        _check_invalid_parameter(kwargs, valid_keys=["global_signal"])

        # set attributes
        self.strategy = strategy
        self.demean = demean
        self.wm_csf = wm_csf
        self.ica_aroma = "full"
        if global_signal:
            self.global_signal = global_signal


def _check_invalid_parameter(keyword_args, valid_keys):
    """Raise warnings if kwargs contains invalid parameters."""
    # supply extra parameter will not effect the behaviour
    # but it is good to inform the user
    for key in valid_keys:
        if isinstance(keyword_args, dict) and key in keyword_args:
            keyword_args.pop(key)
    if isinstance(keyword_args, dict) and len(keyword_args) > 0:
        warnings.warn(
            "Supplied paramerters not accepted in the current "
            "strategy, hence not taking effect: "
            f"{list(keyword_args.keys())}. "
            "Please consider customising strategy with using "
            "the `Confounds` module."
        )


def _update_strategy(strategy, global_signal):
    """Update strategy if global signal is supplied as a parameter."""
    strat = strategy.copy()
    if isinstance(global_signal, str):
        strat.append("global")
    return strat, global_signal
