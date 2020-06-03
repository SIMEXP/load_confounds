import os
import load_confounds as lc
import pandas as pd
import pytest


def _load_test_data():
    path_data = os.path.join(os.path.dirname(lc.__file__), "data")
    return os.path.join(path_data, "confounds.tsv")


def test_minimal():
    file_confounds = _load_test_data()

    # Try to load the confounds, whithout PCA reduction
    conf = lc.load_confounds(file_confounds, strategy="minimal")

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
    conf = lc.load_confounds([file_confounds, file_confounds], strategy="minimal")
    assert isinstance(conf, list)
    assert isinstance(conf[0], pd.DataFrame)
    assert len(conf) == 2


def test_motion():
    file_confounds = _load_test_data()
    conf_basic = lc.load_confounds(file_confounds, strategy="minimal", motion="basic")
    conf_derivatives = lc.load_confounds(
        file_confounds, strategy="minimal", motion="derivatives"
    )
    conf_power2 = lc.load_confounds(file_confounds, strategy="minimal", motion="power2")
    conf_full = lc.load_confounds(file_confounds, strategy="minimal", motion="full")

    params = ["trans_x", "trans_y", "trans_z", "rot_x", "rot_y", "rot_z"]
    for param in params:
        # Basic 6 params motion model
        assert f"{param}" in conf_basic.columns
        assert f"{param}_derivative1" not in conf_basic.columns
        assert f"{param}_power2" not in conf_basic.columns
        assert f"{param}_derivative1_power2" not in conf_basic.columns

        # Use a 6 params + derivatives motion model
        assert f"{param}" in conf_derivatives.columns
        assert f"{param}_derivative1" in conf_derivatives.columns
        assert f"{param}_power2" not in conf_derivatives.columns
        assert f"{param}_derivative1_power2" not in conf_derivatives.columns

        # Use a 6 params + power2 motion model
        assert f"{param}" in conf_power2.columns
        assert f"{param}_derivative1" not in conf_power2.columns
        assert f"{param}_power2" in conf_power2.columns
        assert f"{param}_derivative1_power2" not in conf_power2.columns

        # Use a 6 params + derivatives + power2 + power2d derivatives motion model
        assert f"{param}" in conf_full.columns
        assert f"{param}_derivative1" in conf_full.columns
        assert f"{param}_power2" in conf_full.columns
        assert f"{param}_derivative1_power2" in conf_full.columns


def test_comp_cor():
    file_confounds = _load_test_data()

    conf_compcor_anat = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="anat"
    )
    compcor_col_str_anat = "".join(conf_compcor_anat.columns)
    assert "a_comp_cor_" in compcor_col_str_anat
    assert "t_comp_cor_" not in compcor_col_str_anat

    conf_compcor_temp = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="temp", n_compcor=3
    )
    compcor_col_str_temp = "".join(conf_compcor_temp.columns)
    assert "t_comp_cor_" in compcor_col_str_temp
    assert "a_comp_cor_" not in compcor_col_str_temp

    conf_compcor_full = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="full", n_compcor=3
    )
    compcor_col_str_full = "".join(conf_compcor_full.columns)
    assert "t_comp_cor_" in compcor_col_str_full
    assert "a_comp_cor_" in compcor_col_str_full


def test_ncompcor():

    file_confounds = _load_test_data()

    conf_compcor_0 = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="anat", n_compcor=0
    )
    compcor_col_str_0 = "".join(conf_compcor_0.columns)
    assert "comp_cor_00" in compcor_col_str_0
    assert "comp_cor_01" not in compcor_col_str_0

    conf_compcor_10 = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="anat", n_compcor=10
    )
    compcor_col_str_10 = "".join(conf_compcor_10.columns)
    assert "comp_cor_10" in compcor_col_str_10
    assert "comp_cor_100" not in compcor_col_str_10

    conf_compcor_101 = lc.load_confounds(
        file_confounds, strategy="compcor", compcor="anat", n_compcor=101
    )
    compcor_col_str_101 = "".join(conf_compcor_101.columns)
    assert "comp_cor_101" in compcor_col_str_101
    assert "comp_cor_102" not in compcor_col_str_101


def test_warning():
    file_confounds = _load_test_data()
    with pytest.warns(UserWarning):
        conf_compcor_all = lc.load_confounds(
            file_confounds, strategy="compcor", compcor="temp", n_compcor=4
        )

        compcor_col_str_all = "".join(conf_compcor_all.columns)
        assert "comp_cor_00" in compcor_col_str_all
        assert "comp_cor_01" in compcor_col_str_all
        assert "comp_cor_02" in compcor_col_str_all
        assert "comp_cor_03" in compcor_col_str_all
        assert "comp_cor_04" not in compcor_col_str_all
