from load_confounds import load_confounds 
import json 

json_confound_out = open('confound_out_dict_minimal.json',"r") 
confound_out_dict = json.load(json_confound_out) 

def test_confound_loader_minimal_6params_50(): 
   confound_out = confound_out_dict['confound_loader_minimal_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_minimal_6params_80(): 
   confound_out = confound_out_dict['confound_loader_minimal_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_minimal_6params_95(): 
   confound_out = confound_out_dict['confound_loader_minimal_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_minimal_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_minimal_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_minimal_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_minimal_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_minimal_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_minimal_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_minimal_square_50(): 
   confound_out = confound_out_dict['confound_loader_minimal_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_minimal_square_80(): 
   confound_out = confound_out_dict['confound_loader_minimal_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_minimal_square_95(): 
   confound_out = confound_out_dict['confound_loader_minimal_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_minimal_full_50(): 
   confound_out = confound_out_dict['confound_loader_minimal_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_minimal_full_80(): 
   confound_out = confound_out_dict['confound_loader_minimal_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_minimal_full_95(): 
   confound_out = confound_out_dict['confound_loader_minimal_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["minimal"], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


