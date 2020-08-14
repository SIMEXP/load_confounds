import os
import load_confounds.parser as lc
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


def _regression(confounds):
    """Simple regression with nilearn."""
    # Simulate data
    img, mask_conf, _, _ = _simu_img(demean=True)
    # Do the regression
    masker = NiftiMasker(mask_img=mask_conf, standardize=True)
    tseries_clean = masker.fit_transform(img, confounds=confounds)
    assert tseries_clean.shape[0] == confounds.shape[0]


def test_nilearn_regress():
    """Try regressing out all motion types in nilearn."""
    # Regress full motion
    confounds = lc.Confounds(strategy=["motion"], motion="full").load(file_confounds)
    _regression(confounds)

    # Regress high_pass
    confounds = lc.Confounds(strategy=["high_pass"]).load(file_confounds)
    _regression(confounds)

    # Regress wm_csf
    confounds = lc.Confounds(strategy=["wm_csf"], wm_csf="full").load(file_confounds)
    _regression(confounds)

    # Regress global
    confounds = lc.Confounds(strategy=["global"], global_signal="full").load(
        file_confounds
    )
    _regression(confounds)

    # Regress AnatCompCor
    confounds = lc.Confounds(strategy=["compcor"], compcor="anat").load(file_confounds)
    _regression(confounds)

    # Regress TempCompCor
    confounds = lc.Confounds(strategy=["compcor"], compcor="temp").load(file_confounds)
    _regression(confounds)


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
        lc.Confounds(strategy="string")

    with pytest.raises(ValueError):
        lc.Confounds(strategy=["error"])

    with pytest.raises(ValueError):
        lc.Confounds(strategy=[0])


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
