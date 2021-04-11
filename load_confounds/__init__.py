"""loading fMRIprep confounds into python."""
from load_confounds.parser import Confounds
from load_confounds.strategies import (
    Params2,
    Params6,
    Params9,
    Params9Scrub,
    Params24,
    Params36,
    Params36Scrub,
    AnatCompCor,
    TempCompCor,
    ICAAROMA,
    AROMAGSR,
    AggrICAAROMA,
)

__all__ = [
    "Confounds",
    "Params2",
    "Params6",
    "Params9",
    "Params9Scrub",
    "Params24",
    "Params36",
    "Params36Scrub",
    "AnatCompCor",
    "TempCompCor",
    "ICAAROMA",
    "AROMAGSR",
    "AggrICAAROMA",
]
