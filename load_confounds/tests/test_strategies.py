"""Test predefined denoising strategies."""
import os
import load_confounds.strategies as lc
import numpy as np

path_data = os.path.join(os.path.dirname(lc.__file__), "data")
file_confounds = os.path.join(path_data, "test_desc-confounds_regressors.tsv")


def test_Params2():
    """Test the Params2 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params2()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, np.ndarray)

    # Check that all model categories have been successfully loaded
    list_check = [
        "cosine00",
        "cosine01",
        "cosine02",
        "cosine03",
        "cosine04",
        "cosine05",
        "cosine06",
        "cosine07",
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

    # Check that the confonds is a data frame
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

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, np.ndarray)

    # Check that all model categories have been successfully loaded
    list_check = [
        "trans_y",
        "trans_z",
        "rot_z",
        "cosine00",
        "cosine04",
        "cosine05",
        "csf",
        "white_matter",
        "global_signal",
    ]
    for check in list_check:
        assert check in conf.columns_


def test_Params24():
    """Test the Params24 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params24()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
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
        "cosine04",
        "cosine05",
        "cosine06",
    ]
    for check in list_check:
        assert check in conf.columns_


def test_Params36():
    """Test the Params36 strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params36()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
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
        "cosine06",
        "cosine07",
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


def test_AnatCompCor():
    """Test the AnatCompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.AnatCompCor()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
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
        "cosine05",
        "cosine06",
        "cosine07",
        "a_comp_cor_00",
        "a_comp_cor_01",
        "a_comp_cor_02",
        "a_comp_cor_10",
    ]

    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "t_comp_cor_" not in compcor_col_str_anat


def test_TempCompCor():
    """Test the TempCompCor strategy."""
    # Try to load the confounds, whithout PCA reduction
    conf = lc.TempCompCor()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, np.ndarray)

    list_check = [
        "cosine00",
        "cosine01",
        "cosine02",
        "cosine03",
        "cosine04",
        "cosine05",
        "cosine06",
        "cosine07",
        "t_comp_cor_00",
        "t_comp_cor_01",
        "t_comp_cor_02",
        "t_comp_cor_03",
        "t_comp_cor_04",
        "t_comp_cor_05",
        "t_comp_cor_06",
    ]
    for check in list_check:
        assert check in conf.columns_

    compcor_col_str_anat = "".join(conf.columns_)
    assert "a_comp_cor_" not in compcor_col_str_anat
