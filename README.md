# fmriprep_confound_loader

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1da186ba5c44489b8af6d96a9c50d3c7)](https://app.codacy.com/gh/SIMEXP/fmriprep_load_confounds?utm_source=github.com&utm_medium=referral&utm_content=SIMEXP/fmriprep_load_confounds&utm_campaign=Badge_Grade_Dashboard)

[![codecov](https://codecov.io/gh/SIMEXP/load_confounds/branch/master/graph/badge.svg)](https://codecov.io/gh/SIMEXP/load_confounds)

This package was developed by the SIMEXP Lab. It is used to create a matrix of confound variables from [FMRIPREP](https://fmriprep.readthedocs.io/en/stable/) bold confounds. Users have the option of implementing several strageties based on which parameters they would like to use.

In order to use `load_confounds` it needs to be installed as a python environment (Python >=3.5) using `pip `

` pip install load_confounds`

This module can then be imported: `import load_confounds`


Take the following tsv file sub-01_ses-001.tsv with the following confounds.
![https://user-images.githubusercontent.com/26352860/69464997-f0187900-0d4d-11ea-8d05-02b2c783ef24.png](https://user-images.githubusercontent.com/26352860/69464997-f0187900-0d4d-11ea-8d05-02b2c783ef24.png)

`confounds_out = load_confounds( path/to/file/sub-01_ses-001.tsv , strategy=["minimal"], n_components=0.95, motion_model="6params")`

The default setting selects confounds using a minimal strategy ; the low frequency drifts removed with high-pass filtering, reduced motion parameters from PCA , white matter and csf averages.

![image](https://user-images.githubusercontent.com/26352860/69466742-4dfb8f80-0d53-11ea-94c7-44cb3c1adb7d.png)
