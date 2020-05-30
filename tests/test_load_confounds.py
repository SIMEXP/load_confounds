import os
from nilearn import datasets
import load_confounds as lc

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
