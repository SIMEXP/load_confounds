"""Test predefined denoising strategies."""
import os
import re
import load_confounds.strategies as lc
import numpy as np
import pytest


path_data = os.path.join(os.path.dirname(lc.__file__), "data")
file_confounds = os.path.join(
    path_data, "test_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
)
file_aroma = os.path.join(
    path_data, "test_space-MNI152NLin2009cAsym_desc-smoothAROMAnonaggr_bold.nii.gz"
)


def test_Minimal():
    """Test the Minimal strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Minimal()
    assert conf.strategy == ["high_pass", "motion", "wm_csf"]
    assert hasattr(conf, "global_signal") == False
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    # Check that all model categories have been successfully loaded
    list_check = [
        "trans_y",
        "trans_z",
        "rot_z",
        "cosine00",
        "csf",
        "white_matter",
    ]
    for check in list_check:
        assert check in conf.columns_

    # maker sure global signal works
    conf = lc.Minimal(global_signal="basic")
    assert conf.strategy == ["high_pass", "motion", "wm_csf", "global"]
    assert conf.global_signal == "basic"


def test_Scrubbing():
    """Test the Scrubbing strategy."""
    conf = lc.Scrubbing(fd_thresh=0.15)
    # make sure global signal is not there
    assert conf.strategy == ["high_pass", "motion", "wm_csf", "scrub"]
    assert hasattr(conf, "global_signal") == False
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    # Check that all model categories have been successfully loaded
    list_check = [
        "trans_x",
        "trans_y",
        "rot_z",
        "trans_x_derivative1",
        "trans_x_power2",
        "trans_x_derivative1_power2",
        "trans_y_derivative1",
        "trans_y_power2",
        "trans_y_derivative1_power2",
        "trans_z_derivative1",
        "trans_z_power2",
        "rot_z_derivative1",
        "rot_z_power2",
        "rot_z_derivative1_power2",
        "cosine00",
        "cosine01",
        "csf",
        "white_matter",
        "csf_derivative1",
        "csf_power2",
        "csf_derivative1_power2",
        "white_matter_derivative1",
        "motion_outlier_0",
        "motion_outlier_1",
    ]

    for check in list_check:
        assert check in conf.columns_

    # also load confounds with very liberal scrubbing thresholds
    # this should not produce an error
    conf = lc.Scrubbing(fd_thresh=1, std_dvars_thresh=5)
    conf.load(file_confounds)
    assert "motion_outlier_0" not in conf.columns_

    # maker sure global signal works
    conf = lc.Scrubbing(global_signal="full")
    assert conf.strategy == ["high_pass", "motion", "wm_csf", "scrub", "global"]
    assert conf.global_signal == "full"



def test_CompCor_anatomical():
    """Test the anatomical CompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.CompCor()
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    list_check = [
        "trans_x",
        "trans_y",
        "rot_z",
        "trans_x_derivative1",
        "trans_x_power2",
        "trans_y_derivative1_power2",
        "trans_z_derivative1",
        "trans_z_power2",
        "trans_z_derivative1_power2",
        "rot_y_derivative1",
        "rot_y_power2",
        "rot_z_power2",
        "rot_z_derivative1_power2",
        "cosine00",
        "cosine01",
        "a_comp_cor_00",
        "a_comp_cor_01",
        "a_comp_cor_02",
    ]

    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "t_comp_cor_" not in compcor_col_str_anat
    assert (
        "a_comp_cor_57" not in compcor_col_str_anat
    )  # this one comes from the WW mask


def test_CompCor_anatomical_not_combined():
    """Test the anatomical CompCor strategy without combined mask."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.CompCor(acompcor_combined=False, n_compcor=5)
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    list_check = [
        "trans_x",
        "trans_y",
        "rot_z",
        "trans_x_derivative1",
        "trans_x_power2",
        "trans_y_derivative1_power2",
        "trans_z_derivative1",
        "trans_z_power2",
        "trans_z_derivative1_power2",
        "rot_y_derivative1",
        "rot_y_power2",
        "rot_z_power2",
        "rot_z_derivative1_power2",
        "cosine00",
        "cosine01",
        "a_comp_cor_57",  # from CSF mask
        "a_comp_cor_61",  # from CSF mask
        "a_comp_cor_70",  # from WM mask
        "a_comp_cor_74",  # from WM mask
    ]

    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "t_comp_cor_" not in compcor_col_str_anat
    assert (
        "a_comp_cor_00" not in compcor_col_str_anat
    )  # this one comes from the combined mask
    assert (
        "a_comp_cor_62" not in compcor_col_str_anat
    )  # this one exceeds the number of requested components
    assert (
        "a_comp_cor_75" not in compcor_col_str_anat
    )  # this one exceeds the number of requested components


def test_CompCor_temporal():
    """Test the temporal ompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.CompCor(compcor="temp")
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    list_check = [
        "cosine00",
        "cosine01",
        "cosine02",
        "cosine03",
        "t_comp_cor_00",
        "t_comp_cor_01",
        "t_comp_cor_02",
        "t_comp_cor_03",
    ]
    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "a_comp_cor_" not in compcor_col_str_anat


def test_FullCompCor():
    """Test a full compcor strategy."""
    conf = lc.CompCor(compcor="full", acompcor_combined=False)
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    list_check = [
        "t_comp_cor_00",
        "t_comp_cor_01",
        "t_comp_cor_02",
        "t_comp_cor_03",
        "a_comp_cor_57",  # from CSF mask
        "a_comp_cor_58",  # from CSF mask
        "a_comp_cor_105",  # from WM mask
    ]
    for check in list_check:
        assert check in conf.columns_


def test_ICAAROMA():
    """Test the (non-aggressive) ICA-AROMA strategy."""
    conf = lc.ICAAROMA(global_signal="basic")
    assert conf.global_signal == "basic"
    assert conf.strategy == ["wm_csf", "high_pass", "ica_aroma", "global"]
    conf.load(file_aroma)

    # Check that all fixed name model categories have been successfully loaded
    list_check = [
        "csf",
        "white_matter",
        "global_signal",
    ]
    for c in conf.columns_:
        # Check that all fixed name model categories
        fixed = c in list_check
        cosines = re.match("cosine+", c)
        assert fixed or (cosines is not None)


def test_invalid():
    """Test warning raised for invalid keywors."""
    with pytest.warns(UserWarning) as record:
        lc.ICAAROMA(compcor="anat", global_signal="full")
    assert "not taking effect: ['compcor']" in record[0].message.args[0]
