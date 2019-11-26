# fmriprep_confound_loader

This package was developed by the SIMEXP Lab. It is used to create a matrix of confound variables from [FMRIPREP](https://fmriprep.readthedocs.io/en/stable/) bold confounds. Users have the option of implementing several strageties based on which parameters they would like to use. 

Take the following tsv file sub-01_ses-001.tsv with the following confounds. 
![https://user-images.githubusercontent.com/26352860/69464997-f0187900-0d4d-11ea-8d05-02b2c783ef24.png](https://user-images.githubusercontent.com/26352860/69464997-f0187900-0d4d-11ea-8d05-02b2c783ef24.png)

`confounds_out = load_confounds( path/to/file/sub-01_ses-001.tsv , strategy=["minimal"], n_components=0.95, motion_model="6params")`

The default setting selects confounds using a minimal strategy ; the low frequency drifts removed with high-pass filtering, reduced motion parameters from PCA , white matter and csf averages.

![image](https://user-images.githubusercontent.com/26352860/69466742-4dfb8f80-0d53-11ea-94c7-44cb3c1adb7d.png)
