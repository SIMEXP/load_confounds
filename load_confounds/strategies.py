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
    This strategy can only be performed on output `*desc-smoothAROMAnonaggr_bold`.

    The current implementation is inline with simulation results of fmriprep-notebooks 05.
    https://github.com/nipreps/fmriprep-notebooks/

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
        self.strategy = ["wm_csf", "high_pass"]
        self.demean = demean
        self.wm_csf = "basic"


class AROMAGSR(Confounds):
    """
    Load confounds for post-non-aggresive AROMA-GSR strategy from Ciric et al. 2017.
    This strategy can only be performed on output `*desc-smoothAROMAnonaggr_bold`.

    The current implementation is inline with simulation results of fmriprep-notebooks 05.
    https://github.com/nipreps/fmriprep-notebooks/

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
        self.strategy = ["wm_csf", "high_pass", "global"]
        self.global_signal = "basic"
        self.wm_csf = "basic"
        self.demean = demean


class AggrICAAROMA(Confounds):
    """
    Load confounds for aggresive ICA-AROMA strategy described in Prium et al. 2015.
    This strategy can only be performed on output `*desc-prepro_bold`.

    The current implementation is inline with simulation results of fmriprep-notebooks 05.
    https://github.com/nipreps/fmriprep-notebooks/

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
        self.strategy = ["wm_csf", "high_pass", "global", "ica_aroma"]
        self.global_signal = "basic"
        self.wm_csf = "basic"
        self.demean = demean
