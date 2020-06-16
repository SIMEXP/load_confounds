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


def _simu_img(demean=True):
    """Simulate an nifti image with some parts confounds and some parts noise."""
    # set the size of the image matrix
    nx = 5
    ny = 5
    # the actual number of slices will actually be double of that
    # as we will stack slices with confounds on top of slices with noise
    nz = 2
    # Load a simple 6 parameters motion models as confounds
    X = lc.Confounds(strategy=["motion"], motion="basic", demean=demean).load(
        file_confounds
    )

    # the number of time points is based on the example confound file
    nt = X.shape[0]
    # initialize an empty 4D volume
    vol = np.zeros([nx, ny, 2 * nz, nt])
    vol_conf = np.zeros([nx, ny, 2 * nz])
    vol_rand = np.zeros([nx, ny, 2 * nz])

    # create a random mixture of confounds
    # standardized to zero mean and unit variance
    beta = np.random.rand(nx * ny * nz, X.shape[1])
    tseries_conf = scale(np.matmul(beta, X.transpose()), axis=1)
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

    return img, mask_conf, mask_rand, X


def _tseries_std(img, mask_img, confounds, standardize):
    """Get the std of time series in a mask."""
    masker = NiftiMasker(mask_img=mask_img, standardize=standardize)
    tseries = masker.fit_transform(img, confounds=confounds)
    return tseries.std(axis=0)


def _denoise(img, mask_img, confounds, standardize):
    """Extract time series with and without confounds."""
    masker = NiftiMasker(mask_img=mask_img, standardize=standardize)
    tseries_raw = masker.fit_transform(img)
    tseries_clean = masker.fit_transform(img, confounds=confounds)
    return tseries_raw, tseries_clean


def _corr_tseries(tseries1, tseries2):
    """Compute the correlation between two sets of time series."""
    corr = np.zeros(tseries1.shape[1])
    for ind in range(tseries1.shape[1]):
        corr[ind], _ = pearsonr(tseries1[:, ind], tseries2[:, ind])
    return corr


def test_nilearn_standardize_false():
    """Test removing confounds in nilearn with no standardization."""
    # Simulate data
    img, mask_conf, mask_rand, X = _simu_img(demean=True)

    # Check that most variance is removed
    # in voxels composed of pure confounds
    tseries_std = _tseries_std(img, mask_conf, X, False)
    assert np.mean(tseries_std < 0.0001)

    # Check that most variance is preserved
    # in voxels composed of random noise
    tseries_std = _tseries_std(img, mask_rand, X, False)
    assert np.mean(tseries_std > 0.9)


def test_nilearn_standardize_zscore():
    """Test removing confounds in nilearn with zscore standardization."""
    # Simulate data
    img, mask_conf, mask_rand, X = _simu_img(demean=True)

    # We now load the time series with vs without confounds
    # in voxels composed of pure confounds
    # the correlation before and after denoising should be very low
    # as most of the variance is removed by denoising
    tseries_raw, tseries_clean = _denoise(img, mask_conf, X, "zscore")
    corr = _corr_tseries(tseries_raw, tseries_clean)
    assert corr.mean() < 0.2

    # We now load the time series with zscore standardization
    # with vs without confounds in voxels where the signal is uncorrelated
    # with confounds. The correlation before and after denoising should be very
    # high as very little of the variance is removed by denoising
    tseries_raw, tseries_clean = _denoise(img, mask_rand, X, "zscore")
    corr = _corr_tseries(tseries_raw, tseries_clean)
    assert corr.mean() > 0.8


def test_nilearn_standardize_psc():
    """Test removing confounds in nilearn with psc standardization."""
    # Similar test to test_nilearn_standardize_zscore, but with psc
    # Simulate data
    img, mask_conf, mask_rand, X = _simu_img(demean=False)

    # Areas with
    tseries_raw, tseries_clean = _denoise(img, mask_conf, X, "psc")
    corr = _corr_tseries(tseries_raw, tseries_clean)
    assert corr.mean() < 0.2

    # Areas with random noise
    tseries_raw, tseries_clean = _denoise(img, mask_rand, X, "psc")
    corr = _corr_tseries(tseries_raw, tseries_clean)
    assert corr.mean() > 0.8


def test_read_file():
    """Check that loading missing or incomplete files produce error messages."""
    conf = lc.Confounds()
    with pytest.raises(FileNotFoundError):
        conf.load(" ")

    with pytest.raises(ValueError):
        df = pd.read_csv(file_confounds, sep="\t")
        df = df.drop("trans_x", axis=1)
        conf.load(df)


def test_confounds2df():
    """Check auto-detect of confonds from an fMRI nii image."""
    conf = lc.Confounds()
    file_confounds_nii = os.path.join(
        path_data, "test_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"
    )
    conf.load(file_confounds_nii)
    assert "trans_x" in conf.columns_


def test_sanitize_strategy():
    """Check that flawed strategy options generate meaningful error messages."""
    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy="string")

    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy=["error"])

    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy=[0])


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


def test_motion():

    conf_basic = lc.Confounds(strategy=["motion"], motion="basic")
    conf_basic.load(file_confounds)
    conf_derivatives = lc.Confounds(strategy=["motion"], motion="derivatives")
    conf_derivatives.load(file_confounds)
    conf_power2 = lc.Confounds(strategy=["motion"], motion="power2")
    conf_power2.load(file_confounds)
    conf_full = lc.Confounds(strategy=["motion"], motion="full")
    conf_full.load(file_confounds)

    params = ["trans_x", "trans_y", "trans_z", "rot_x", "rot_y", "rot_z"]
    for param in params:
        # Basic 6 params motion model
        assert f"{param}" in conf_basic.columns_
        assert f"{param}_derivative1" not in conf_basic.columns_
        assert f"{param}_power2" not in conf_basic.columns_
        assert f"{param}_derivative1_power2" not in conf_basic.columns_

        # Use a 6 params + derivatives motion model
        assert f"{param}" in conf_derivatives.columns_
        assert f"{param}_derivative1" in conf_derivatives.columns_
        assert f"{param}_power2" not in conf_derivatives.columns_
        assert f"{param}_derivative1_power2" not in conf_derivatives.columns_

        # Use a 6 params + power2 motion model
        assert f"{param}" in conf_power2.columns_
        assert f"{param}_derivative1" not in conf_power2.columns_
        assert f"{param}_power2" in conf_power2.columns_
        assert f"{param}_derivative1_power2" not in conf_power2.columns_

        # Use a 6 params + derivatives + power2 + power2d derivatives motion model
        assert f"{param}" in conf_full.columns_
        assert f"{param}_derivative1" in conf_full.columns_
        assert f"{param}_power2" in conf_full.columns_
        assert f"{param}_derivative1_power2" in conf_full.columns_


def test_n_motion():

    conf = lc.Confounds(strategy=["motion"], motion="full", n_motion=0.2)
    conf.load(file_confounds)
    assert "motion_pca_1" in conf.columns_
    assert "motion_pca_2" not in conf.columns_

    conf = lc.Confounds(strategy=["motion"], motion="full", n_motion=0.95)
    conf.load(file_confounds)
    assert "motion_pca_6" in conf.columns_

    with pytest.raises(ValueError):
        conf = lc.Confounds(strategy=["motion"], motion="full", n_motion=50)
        conf.load(file_confounds)
