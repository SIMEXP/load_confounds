import os
import load_confounds as lc
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import scale
import pytest
from nibabel import Nifti1Image
from nilearn.input_data import NiftiMasker

path_data = os.path.join(os.path.dirname(lc.__file__), "data")
file_confounds = os.path.join(path_data, "test_desc-confounds_regressors.tsv")


def _simu_img():
    # set the size of the image matrix
    nx = 5
    ny = 5
    # the actual number of slices will actually be double of that
    # as we will stack slices with confounds on top of slices with noise
    nz = 2
    # Load a simple 6 parameters motion models as confounds
    conf = lc.Confounds(strategy=["motion"], motion="basic")
    X = conf.load(file_confounds)
    # the number of time points is based on the example confound file
    nt = X.shape[0]
    # initialize an empty 4D volume
    vol = np.zeros([nx, ny, 2 * nz, nt])
    vol_conf = np.zeros([nx, ny, 2 * nz])
    vol_rand = np.zeros([nx, ny, 2 * nz])

    # create a random mixture of confounds
    # standardized to zero mean and unit variance
    beta = np.random.rand(nx * ny * nz, X.shape[1])
    tseries_conf = scale(np.matmul(beta,X.values.transpose()), axis=1)
    # fill the first half of the 4D data with the mixture
    vol[:, :, 0:nz, :] = tseries_conf.reshape(nx, ny, nz, nt)
    vol_conf[:, :, 0:nz] = 1

    # create random noise in the second half of the 4D data
    tseries_rand = scale(np.random.randn(nx * ny * nz, nt), axis=1)
    vol[:, :, range(nz, 2 * nz), :] = tseries_rand.reshape(nx, ny, nz, nt)
    vol_rand[:, :, range(nz, 2 * nz)] = 1

    # Shift the mean to non-zero
    vol = vol + 100

    # create an nifti image with the data, and corresponding mask
    img = Nifti1Image(vol, np.eye(4))
    mask_conf = Nifti1Image(vol_conf, np.eye(4))
    mask_rand = Nifti1Image(vol_rand, np.eye(4))

    return img, mask_conf, mask_rand


def test_denoise_nilearn():
    img, mask_conf, mask_rand = _simu_img()
    conf = lc.Confounds(strategy=["motion"], motion="basic")
    X = conf.load(file_confounds)

    # We first mask the voxel where there are only confounds
    masker = NiftiMasker(mask_img=mask_conf, standardize=False)
    tseries = masker.fit_transform(img, confounds=conf.confounds_.values)
    tseries_std = tseries.std(axis=0)
    # First half of time series should have close to zero variance
    # as they were composed of pure confounds
    for val in tseries_std:
        assert val < 0.01

    # We now mask the voxel where there is signal uncorrelated to confounds
    masker = NiftiMasker(mask_img=mask_rand, standardize=False)
    tseries = masker.fit_transform(img, confounds=conf.confounds_.values)
    tseries_std = tseries.std(axis=0)
    # The variance should be at least 0.5, as the confounds are uncorrelated
    # with the signal
    for val in tseries_std:
        assert val >0.5

    # We now load the time series with zscore standardization
    # with vs without confounds
    # in voxels where there are only confounds
    masker = NiftiMasker(mask_img=mask_conf, standardize="zscore")
    tseries_raw = masker.fit_transform(img)
    tseries_clean = masker.fit_transform(img, confounds=conf.confounds_.values)
    # the correlation before and after denoising should be very low
    # as most of the variance is removed by denoising
    for ind in range(tseries_raw.shape[1]):
        corr, _ = pearsonr(tseries_raw[:, ind], tseries_clean[:, ind])
        assert corr < 0.5

    # We now load the time series with zscore standardization
    # with vs without confounds
    # in voxels where the signal is uncorrelated with confounds
    masker = NiftiMasker(mask_img=mask_rand, standardize="zscore")
    tseries_raw = masker.fit_transform(img)
    tseries_clean = masker.fit_transform(img, confounds=conf.confounds_.values)
    # the correlation before and after denoising should be very low
    # as most of the variance is removed by denoising
    for ind in range(tseries_raw.shape[1]):
        corr, _ = pearsonr(tseries_raw[:, ind], tseries_clean[:, ind])
        assert corr > 0.5


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


def test_Params2():

    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params2()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns


def test_Params9():

    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params9()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns


def test_Params24():

    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params24()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns


def test_Params36():

    # Try to load the confounds, whithout PCA reduction
    conf = lc.Params36()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns


def test_AnatCompCor():
    # Try to load the confounds, whithout PCA reduction
    conf = lc.AnatCompCor()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns

    compcor_col_str_anat = "".join(conf.confounds_.columns)
    assert "t_comp_cor_" not in compcor_col_str_anat


def test_TempCompCor():
    # Try to load the confounds, whithout PCA reduction
    conf = lc.TempCompCor()
    conf.load(file_confounds)

    # Check that the confonds is a data frame
    assert isinstance(conf.confounds_, pd.DataFrame)

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
        assert check in conf.confounds_.columns

    compcor_col_str_anat = "".join(conf.confounds_.columns)
    assert "a_comp_cor_" not in compcor_col_str_anat
