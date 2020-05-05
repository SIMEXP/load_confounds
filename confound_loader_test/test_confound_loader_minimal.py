from load_confounds import load_confounds


def test_confound_loader_minimal_6params_80():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="6params",
            n_components=0.80,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_6params_50():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="6params",
            n_components=0.50,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_6params_95():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="6params",
            n_components=0.95,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_derivatives_80():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="derivatives",
            n_components=0.80,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
            "motion_pca_2",
        ]
    )


def test_confound_loader_minimal_derivatives_50():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="derivatives",
            n_components=0.50,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_derivatives_95():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="derivatives",
            n_components=0.95,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
            "motion_pca_2",
        ]
    )


def test_confound_loader_minimal_square_80():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="square",
            n_components=0.80,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_square_50():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="square",
            n_components=0.50,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_square_95():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="square",
            n_components=0.95,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_full_80():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="full",
            n_components=0.80,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
            "motion_pca_2",
        ]
    )


def test_confound_loader_minimal_full_50():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="full",
            n_components=0.50,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
        ]
    )


def test_confound_loader_minimal_full_95():
    assert set(
        load_confounds(
            confounds_raw="sub-01_ses-001.tsv",
            strategy=["minimal"],
            motion_model="full",
            n_components=0.95,
        ).columns.values
    ) == set(
        [
            "csf_power2",
            "cosine01",
            "csf_derivative1_power2",
            "white_matter_derivative1_power2",
            "cosine05",
            "white_matter_derivative1",
            "cosine03",
            "cosine07",
            "cosine06",
            "csf_derivative1",
            "cosine02",
            "cosine00",
            "cosine04",
            "white_matter_power2",
            "white_matter",
            "csf",
            "motion_pca_1",
            "motion_pca_2",
        ]
    )
