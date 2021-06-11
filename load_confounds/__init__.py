"""loading fMRIprep confounds into python."""
from load_confounds.parser import Confounds
from load_confounds.strategies import (
    Minimal,
    Scrubbing,
    CompCor,
    ICAAROMA,
)

__all__ = [
    "Confounds",
    "Minimal",
    "Scrubbing",
    "CompCor",
    "ICAAROMA",
]
