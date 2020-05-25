from load_confounds import load_confounds 
import json 

json_confound_out = open('confound_out_dict.json',"r") 
confound_out_dict = json.load(json_confound_out) 

def test_confound_loader_compcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_compcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_compcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_compcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_compcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_compcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_compcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_compcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_compcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_compcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_compcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_compcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_compcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_compcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_compcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_compcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_compcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_compcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_compcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_compcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_compcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_compcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_compcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_compcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["compcor"], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_matter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_matter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_matter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_matter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_matter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_matter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_matter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_matter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_matter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_matter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_matter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_matter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_matter_square_80(): 
   confound_out = confound_out_dict['confound_loader_matter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_matter_square_50(): 
   confound_out = confound_out_dict['confound_loader_matter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_matter_square_95(): 
   confound_out = confound_out_dict['confound_loader_matter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_matter_full_80(): 
   confound_out = confound_out_dict['confound_loader_matter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_matter_full_50(): 
   confound_out = confound_out_dict['confound_loader_matter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_matter_full_95(): 
   confound_out = confound_out_dict['confound_loader_matter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["matter"], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_mattercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_mattercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['matter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_square_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_square_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_square_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_full_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_full_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filter_full_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["high_pass_filter"], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_square_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_square_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_square_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_full_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_full_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermatter_full_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermatter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_high_pass_filtermattercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_high_pass_filtermattercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motion_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motion_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motion_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motion_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motion_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motion_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motion_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motion_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motion_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motion_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motion_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motion_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motion_square_80(): 
   confound_out = confound_out_dict['confound_loader_motion_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motion_square_50(): 
   confound_out = confound_out_dict['confound_loader_motion_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motion_square_95(): 
   confound_out = confound_out_dict['confound_loader_motion_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motion_full_80(): 
   confound_out = confound_out_dict['confound_loader_motion_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motion_full_50(): 
   confound_out = confound_out_dict['confound_loader_motion_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motion_full_95(): 
   confound_out = confound_out_dict['confound_loader_motion_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ["motion"], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motioncompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_motioncompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmatter_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionmatter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionmattercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionmattercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'matter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filter_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermatter_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermatter_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_6params_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_6params_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_6params_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_6params_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_6params_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_6params_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "6params", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_derivatives_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_derivatives_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_derivatives_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_derivatives_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_derivatives_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_derivatives_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "derivatives", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_square_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_square_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_square_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_square_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_square_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_square_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "square", n_components = 0.95).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_full_80(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_full_80'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.80).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_full_50(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_full_50'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.50).columns.values) == set(confound_out)


def test_confound_loader_motionhigh_pass_filtermattercompcor_full_95(): 
   confound_out = confound_out_dict['confound_loader_motionhigh_pass_filtermattercompcor_full_95'] 
   assert set(load_confounds(confounds_raw = "sub-01_ses-001.tsv", strategy = ['motion', 'high_pass_filter', 'matter', 'compcor'], motion_model = "full", n_components = 0.95).columns.values) == set(confound_out)


