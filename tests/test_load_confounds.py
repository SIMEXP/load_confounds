import os
from nilearn import datasets
import load_confounds as lc
import pandas as pd

def _load_test_data():

    path_data = os.path.join(os.path.dirname(lc.__file__), 'data')
    return os.path.join(path_data, 'confounds.tsv')

def test_minimal():
    file_confounds = _load_test_data()

    # Try to load the confounds, whithout PCA reduction
    conf = lc.load_confounds(file_confounds, strategy=['minimal'], n_components=0)

    # Check that all model categories have been successfully loaded
    list_check = ['trans_x', 'rot_x', 'cosine00', 'csf', 'white_matter']
    for check in list_check:
        assert(check in conf.columns)


def test_motion_model():
    file_confounds = _load_test_data()

    # Use a 6 params motion model
    conf = lc.load_confounds(file_confounds, strategy=['minimal'], n_components=0, motion_model="6params")
    assert('trans_x' in conf.columns)
    assert('trans_x_derivative1' not in conf.columns)
    assert('trans_x_power2' not in conf.columns)
    assert('trans_x_derivative1_power2' not in conf.columns)

    # Use a 6 params + derivatives motion model
    conf = lc.load_confounds(file_confounds, strategy=['minimal'], n_components=0, motion_model="derivatives")
    assert('trans_x' in conf.columns)
    assert('trans_x_derivative1' in conf.columns)
    assert('trans_x_power2' not in conf.columns)
    assert('trans_x_derivative1_power2' not in conf.columns)

    # Use a 6 params + square motion model
    conf = lc.load_confounds(file_confounds, strategy=['minimal'], n_components=0, motion_model="square")
    assert('trans_x' in conf.columns)
    assert('trans_x_derivative1' not in conf.columns)
    assert('trans_x_power2' in conf.columns)
    assert('trans_x_derivative1_power2' not in conf.columns)

    # Use a 6 params + square motion model
    conf = lc.load_confounds(file_confounds, strategy=['minimal'], n_components=0, motion_model="full")
    assert('trans_x' in conf.columns)
    assert('trans_x_derivative1' in conf.columns)
    assert('trans_x_power2' in conf.columns)
    assert('trans_x_derivative1_power2' in conf.columns)
