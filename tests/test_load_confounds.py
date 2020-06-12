import os
import load_confounds as lc
import pandas as pd
import pytest


path_data = os.path.join(os.path.dirname(lc.__file__), "data")
file_confounds = os.path.join(path_data, "test_desc-confounds_regressors.tsv")


def test_read_file():
    conf = lc.Confounds()
    with pytest.raises(FileNotFoundError):
        conf.load(" ")

    with pytest.raises(ValueError):
        df = pd.read_csv(file_confounds, sep="\t")
        df = df.drop("trans_x", axis=1)
        conf.load(df)


def test_confounds2df():
    conf = lc.Confounds()
    file_confounds_nii = os.path.join(
        path_data, "test_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
    )
    conf_nii = conf.load(file_confounds_nii)
    assert "trans_x" in conf_nii.columns


def test_sanitize_strategy():
    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy="string")

    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy=["error"])

    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy=[0])


def test_Params6():

    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params6()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

    # Check that all model categories have been successfully loaded
    list_check = [
        "trans_x",
        "trans_y",
        "trans_z",
        "rot_x",
        "rot_y",
        "rot_z",
        "cosine00",
    ]
    for check in list_check:
        assert check in conf.confounds_.columns

    # Load the confounds in a list
    conf.load([file_confounds, file_confounds])
    assert isinstance(conf.confounds_, list)
    assert isinstance(conf.confounds_[0], pd.DataFrame)
    assert len(conf.confounds_) == 2


def test_motion():

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


def test_warning_compcor():

    with pytest.warns(UserWarning):
        conf_compcor_all = lc.load_confounds(
            file_confounds, strategy="compcor", compcor="temp", n_compcor=18
        )

        compcor_col_str_all = "".join(conf_compcor_all.columns)
        assert "comp_cor_00" in compcor_col_str_all
        assert "comp_cor_01" in compcor_col_str_all
        assert "comp_cor_02" in compcor_col_str_all
        assert "comp_cor_03" in compcor_col_str_all
        assert "comp_cor_19" not in compcor_col_str_all


def test_n_motion():

    conf_compcor_fifth = lc.load_confounds(file_confounds, motion="full", n_motion=0.2)
    conf_compcor_fifth = "".join(conf_compcor_fifth.columns)
    assert "motion_pca_1" in conf_compcor_fifth
    assert "motion_pca_2" not in conf_compcor_fifth

    conf_compcor_95 = lc.load_confounds(file_confounds, motion="full", n_motion=0.95)
    conf_compcor_95 = "".join(conf_compcor_95.columns)
    assert "motion_pca_1" in conf_compcor_95
    assert "motion_pca_2" in conf_compcor_95

    conf_compcor_one = lc.load_confounds(file_confounds, motion="full", n_motion=1)
    conf_compcor_one = "".join(conf_compcor_one.columns)
    assert "motion_pca_1" in conf_compcor_one
    assert "motion_pca_2" not in conf_compcor_one

    conf_compcor_two = lc.load_confounds(file_confounds, motion="full", n_motion=2)
    conf_compcor_two = "".join(conf_compcor_two.columns)
    assert "motion_pca_1" in conf_compcor_two
    assert "motion_pca_2" in conf_compcor_two

    conf_compcor_twentyfour = lc.load_confounds(
        file_confounds, motion="full", n_motion=24
    )
    conf_compcor_twentyfour = "".join(conf_compcor_twentyfour.columns)
    assert "motion_pca_1" in conf_compcor_twentyfour
    assert "motion_pca_25" not in conf_compcor_twentyfour

    conf_compcor_twelve = lc.load_confounds(file_confounds, motion="full", n_motion=12)
    conf_compcor_twelve = "".join(conf_compcor_twelve.columns)
    assert "motion_pca_1" in conf_compcor_twelve
    assert "motion_pca_13" not in conf_compcor_twelve

    conf_compcor_zero = lc.load_confounds(file_confounds, motion="full", n_motion=0)
    conf_compcor_zero = "".join(conf_compcor_zero.columns)
    assert "motion_pca_1" not in conf_compcor_zero
    assert "motion_pca_2" not in conf_compcor_zero

    with pytest.raises(ValueError, match="must be between"):
        lc.load_confounds(file_confounds, motion="full", n_motion=50)


def test_load_global():

    conf_global = lc.load_confounds(file_confounds, strategy=["global"])
    assert "global_signal" in conf_global.columns.values


def test_find_confounds():

    df = pd.read_csv(file_confounds, sep="\t")

    # remove the discrete cosines from the confounds
    for label in df.columns:
        if "cosine" in label:
            df = df.drop(label, axis=1)

    # load_confounds should throw in an error
    # because it cannot find variables for high_pass
    with pytest.raises(ValueError, match="could not find any confound with the key"):
        lc.load_confounds(df)


def test_load_high_pass():

    conf_high_pass = lc.load_confounds(file_confounds, strategy=["high_pass"])
    assert "cosine" in conf_high_pass.columns[0]
