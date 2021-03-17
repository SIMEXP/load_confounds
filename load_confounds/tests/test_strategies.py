"""Test predefined denoising strategies."""
import os
import re
import load_confounds.strategies as lc
import numpy as np

path_data = os.path.join(os.path.dirname(lc.__file__), "data")
file_confounds = os.path.join(path_data, "test_desc-confounds_regressors.tsv")


def test_Params2():
    """Test the Params2 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params2()
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

    # Check that all model categories have been successfully loaded
    list_check = [
        "cosine00",
        "cosine01",
        "cosine02",
        "cosine03",
        "csf",
        "white_matter",
    ]
    for check in list_check:
        assert check in conf.columns_


def test_Params6():
    """Test the Params6 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params6()
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

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
        assert check in conf.columns_

    # Load the confounds in a list
    conf.load([file_confounds, file_confounds])
    assert isinstance(conf.confounds_, list)
    assert isinstance(conf.confounds_[0], np.ndarray)
    assert len(conf.confounds_) == 2


def test_Params9():
    """Test the Params9 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params9()
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
        "global_signal",
    ]
    for check in list_check:
        assert check in conf.columns_


def test_Params9Scrub():
    """Test the Params9Scrub strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params9Scrub(fd_thresh=0.15)
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
        "motion_outlier_0",
        "motion_outlier_1",
    ]
    for check in list_check:
        assert check in conf.columns_

    # also load confounds with very liberal scrubbing thresholds
    # this should not produce an error
    conf = lc.Params9Scrub(fd_thresh=1, std_dvars_thresh=5)
    conf.load(file_confounds)
    assert "motion_outlier_0" not in conf.columns_


def test_Params24():
    """Test the Params24 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params24()
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
        "trans_z_derivative1",
        "trans_z_power2",
        "rot_x_power2",
        "rot_y_power2",
        "rot_y_derivative1_power2",
        "rot_z_derivative1",
        "cosine00",
    ]
    for check in list_check:
        assert check in conf.columns_


def test_Params36():
    """Test the Params36 strategy."""
    # Try to load the confounds
    conf = lc.Params36()
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
        "global_signal",
        "global_signal_derivative1",
        "global_signal_power2",
        "global_signal_derivative1_power2",
    ]

    for check in list_check:
        assert check in conf.columns_


def test_Params36Scrub():
    """Test the Params36Scrub strategy."""
    conf = lc.Params36Scrub(fd_thresh=0.15)
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
    conf = lc.Params36Scrub(fd_thresh=1, std_dvars_thresh=5)
    conf.load(file_confounds)
    assert "motion_outlier_0" not in conf.columns_


def test_AnatCompCor():
    """Test the AnatCompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.AnatCompCor()
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


def test_AnatCompCor_not_combined():
    """Test the AnatCompCor strategy without combined mask."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.AnatCompCor(acompcor_combined=False)
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
        "a_comp_cor_58",  # from CSF mask
        "a_comp_cor_105",  # from WM mask
    ]

    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "t_comp_cor_" not in compcor_col_str_anat
    assert (
        "a_comp_cor_00" not in compcor_col_str_anat
    )  # this one comes from the combined mask


def test_TempCompCor():
    """Test the TempCompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.TempCompCor()
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


def test_ICAAROMA():
    """Test the (non-aggressive) ICA-AROMA strategy."""
    conf = lc.ICAAROMA()
    conf.load(file_confounds)

    assert isinstance(conf.confounds_, np.ndarray)

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
        assert fixed or cosines


def test_AROMAGSR():
    """Test the (non-aggressive) AROMA-GSR strategy."""
    conf = lc.AROMAGSR()
    conf.load(file_confounds)

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
        assert fixed or cosines


def test_AggrICAAROMA():
    """Test the aggressive ICA-AROMA strategy."""
    conf = lc.AggrICAAROMA()
    conf.load(file_confounds)

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
        aroma = re.match("aroma_motion_+", c)
        assert fixed or cosines or aroma
