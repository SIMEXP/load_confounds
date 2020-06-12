"""
loading fMRIprep confounds into python
"""
from .load_confounds import (
    Confounds,
    Params2,
    Params6,
    Params9,
    Params24,
    Params36,
    AnatCompCor,
    TempCompCor,
)

__all__ = [
    "Confounds",
    "Params2",
    "Params6",
    "Params9",
    "Params24",
    "Params36",
    "AnatCompCor",
    "TempCompCor",
]
