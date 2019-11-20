import argparse
import glob
import numpy as np
import nibabel as nb
import pathlib as pal
import pandas as pd
import warnings
from sklearn.decomposition import PCA
from nilearn.image import clean_img
from nilearn.input_data import NiftiMasker
from nilearn import datasets

warnings.filterwarnings("ignore", category=DeprecationWarning)

motion = ["trans_x", "trans_y", "trans_z", "rot_x", "rot_y", "rot_z"]
motion_models = {
    "6params": "{}",
    "derivatives": "{}_derivative1",
    "square": "{}_power2",
    "full": "{}_derivative1_power2",
}
compcor = [
    "t_comp_cor_00",
    "t_comp_cor_01",
    "t_comp_cor_02",
    "t_comp_cor_03",
    "t_comp_cor_04",
    "t_comp_cor_05",
    "a_comp_cor_00",
    "a_comp_cor_01",
    "a_comp_cor_02",
    "a_comp_cor_03",
    "a_comp_cor_04",
    "a_comp_cor_05",
]
high_pass_filter = [
    "cosine00",
    "cosine01",
    "cosine02",
    "cosine03",
    "cosine04",
    "cosine05",
    "cosine06",
]

matter = ["csf", "white_matter"]

confound_dict = {
    "motion": motion,
    "matter": matter,
    "high_pass_filter": high_pass_filter,
    "compcor": compcor,
    "minimal": matter + high_pass_filter + motion,
}


def scrub_encode(scrub_paramters):

    frames = 0
    scrub_vol = []

    for vol in scrub_paramters.values:
        if vol == 1:
            scrub_vol_str = "scrub_vol" + str(frames)
            scrub_vol.append(scrub_vol_str)
        else:
            scrub_vol.append(0)
        frames += 1

    scrub_confounds = pd.get_dummies(scrub_vol, drop_first=False)

    scrub_confounds.drop(columns=0, inplace=True)

    return scrub_confounds


def _pca_motion(confounds_full, confounds, n_components=0.95, model="square"):
    """Reduce the motion paramaters using PCA."""

    motion_columns = list(
        set(motion + [motion_models[model].format(col) for col in motion])
    )

    motion_parameters_raw = confounds[motion_columns]

    if n_components == 0:
        motion_confounds = motion_parameters_raw

    else:
        motion_parameters_raw.dropna(inplace=True)
        pca = PCA(n_components=n_components)
        confounds_pca = pca.fit_transform(motion_parameters_raw.values)
        motion_confounds = pd.DataFrame(confounds_pca)
        motion_confounds.columns = [
            "motion_pca_" + str(col + 1) for col in motion_confounds.columns
        ]

    confounds_full.drop(columns=motion, inplace=True)
    confounds_full = pd.concat((confounds_full, motion_confounds), axis=1)

    return confounds_full


def load_confounds(
    confounds_raw, strategy=["minimal"], n_components=0.95, model="full"
):

    if not isinstance(confounds_raw, pd.DataFrame):
        confounds_raw = pd.read_csv(confounds_raw, delimiter="\t", encoding="utf-8")

    confounds_full = pd.DataFrame()
    for strat in strategy:

        # Run PCA on motion parameters
        if strat in confound_dict.keys():

            confounds_full = pd.concat(
                (confounds_full, confounds_raw[confound_dict[strat]]), axis=1
            )
        else:
            confounds_full = pd.concat((confounds_full, confounds_raw[strat]), axis=1)

    if len(confounds_full.columns) != len(set(confounds_full.columns)):
        raise ValueError("Your strategy has duplicate confounds.")

    # motion_bolean = set(motion) & set(confounds_full.columns)

    if set(motion) & set(confounds_full.columns):
        confounds_full = _pca_motion(confounds_full, confounds_raw, n_components, model)

    return confounds_full


if __name__ == "__main__":

    tsv_file = (
        "sub-01_ses-001.tsv"
    )

    confounds_test = load_confounds(
        tsv_file, strategy=["minimal"], model="6params", n_components=0.95
    )
    print(confounds_test)
    confounds_test.to_csv("csv_output/confounds_test.csv", index=False)
