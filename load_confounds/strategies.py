"""Predefined denoising strategies.

Authors: Hanad Sharmarke, Dr. Pierre Bellec, Francois Paugam
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


class AnatCompCor(Confounds):
    """
    Load confounds using the aCOMPCOR strategy from Ciric et al. 2017.
    Motion parameters (fully expanded), high pass filter, and acompcor.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    n_compcor : int, optional
        The number of noise components to be extracted.

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

    def __init__(self, n_compcor=10, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "motion", "compcor"]
        self.motion = "full"
        self.n_motion = 0
        self.compcor = "anat"
        self.n_compcor = n_compcor
        self.demean = demean


class TempCompCor(Confounds):
    """
    Load confounds using the tCOMPCOR strategy from Ciric et al. 2017.
    High pass filter, and tcompcor.

    Parameters
    ----------
    confounds_raw : Pandas Dataframe or path to tsv file(s), optionally as a list.
        Raw confounds from fmriprep

    n_compcor : int, optional
        The number of noise components to be extracted.

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

    def __init__(self, n_compcor=6, demean=True):
        """Default parameters."""
        self.strategy = ["high_pass", "compcor"]
        self.compcor = "temp"
        self.n_compcor = n_compcor
        self.demean = demean
