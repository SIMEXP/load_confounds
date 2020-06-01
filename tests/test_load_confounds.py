import os
from nilearn import datasets
import load_confounds as lc
import pandas as pd


def _load_test_data():
    path_data = os.path.join(os.path.dirname(lc.__file__), "data")
    return os.path.join(path_data, "confounds.tsv")


def test_minimal():
    file_confounds = _load_test_data()

    # Try to load the confounds, whithout PCA reduction
    conf = lc.load_confounds(file_confounds, strategy=["minimal"], n_components=0)

    # Check that the confonds is a data frame
    assert isinstance(conf, pd.DataFrame)

    # Check that all model categories have been successfully loaded
    list_check = [
        "trans_x",
        "trans_y",
        "trans_z",
        "rot_x",
        "rot_y",
        "rot_z",
        "cosine00",
        "csf",
        "white_matter",
    ]
    for check in list_check:
        assert check in conf.columns

    # Load the confounds in a list
    conf = lc.load_confounds(
        [file_confounds, file_confounds], strategy=["minimal"], n_components=0
    )
    assert isinstance(conf, list)
    assert isinstance(conf[0], pd.DataFrame)
    assert len(conf) == 2


def test_motion_model():
    file_confounds = _load_test_data()

    # Use a 6 params motion model
    conf = lc.load_confounds(
        file_confounds, strategy=["minimal"], n_components=0, motion_model="6params"
    )
    params = ["trans_x", "trans_y", "trans_z", "rot_x", "rot_y", "rot_z"]
    for param in params:
        assert f"{param}" in conf.columns
        assert f"{param}_derivative1" not in conf.columns
        assert f"{param}_power2" not in conf.columns
        assert f"{param}_derivative1_power2" not in conf.columns

        # Use a 6 params + derivatives motion model
        conf = lc.load_confounds(
            file_confounds,
            strategy=["minimal"],
            n_components=0,
            motion_model="derivatives",
        )
        assert f"{param}" in conf.columns
        assert f"{param}_derivative1" in conf.columns
        assert f"{param}_power2" not in conf.columns
        assert f"{param}_derivative1_power2" not in conf.columns

        # Use a 6 params + square motion model
        conf = lc.load_confounds(
            file_confounds, strategy=["minimal"], n_components=0, motion_model="square"
        )
        assert f"{param}" in conf.columns
        assert f"{param}_derivative1" not in conf.columns
        assert f"{param}_power2" in conf.columns
        assert f"{param}_derivative1_power2" not in conf.columns

        # Use a 6 params + square motion model
        conf = lc.load_confounds(
            file_confounds, strategy=["minimal"], n_components=0, motion_model="full"
        )
        assert f"{param}" in conf.columns
        assert f"{param}_derivative1" in conf.columns
        assert f"{param}_power2" in conf.columns
        assert f"{param}_derivative1_power2" in conf.columns
