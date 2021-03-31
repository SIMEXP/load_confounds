# load_confounds
Load a sensible subset of the fMRI confounds generated with [fMRIprep](https://fmriprep.readthedocs.io/en/stable/) in python (Esteban et al., 2018). 
*Warning*: This package is at an alpha stage of development. The API may still be subject to changes.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SIMEXP/load_confounds/HEAD?filepath=demo%2Fload_confounds_demo.ipynb) [![All Contributors](https://img.shields.io/badge/all_contributors-10-orange.svg?style=flat-square)](#contributors-) [![collaborate brainhack](https://img.shields.io/badge/collaborate-brainhack-FF69A4.svg)](https://mattermost.brainhack.org/brainhack/channels/fmriprep_denoising) [![Pipy Badge](https://img.shields.io/pypi/v/load_confounds)](https://pypi.org/project/load-confounds/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1da186ba5c44489b8af6d96a9c50d3c7)](https://app.codacy.com/gh/SIMEXP/load_confounds?utm_source=github.com&utm_medium=referral&utm_content=SIMEXP/load_confounds&utm_campaign=Badge_Grade_Dashboard) [![Maintainability](https://api.codeclimate.com/v1/badges/ce6f2bf20aa87accaaa4/maintainability)](https://codeclimate.com/github/SIMEXP/load_confounds/maintainability) [![CircleCI](https://circleci.com/gh/SIMEXP/load_confounds.svg?style=svg)](https://circleci.com/gh/SIMEXP/load_confounds) [![codecov](https://codecov.io/gh/SIMEXP/load_confounds/branch/master/graph/badge.svg)](https://codecov.io/gh/SIMEXP/load_confounds) [![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation 
Install with `pip` (Python >=3.5):
```bash
pip install load_confounds
```

## TL;DR
Load confounds using the 36P denoising strategy of Ciric et al. 2017:
```python
from load_confounds import Params36
from nilearn.input_data import NiftiMasker 

# load_confounds auto-detects the companion .tsv file (which needs to be in the same directory)
file = "path/to/file/sub-01_ses-001_bold.nii.gz"
confounds = Params36().load(file)

# Use the confounds in a nilearn maker 
masker = NiftiMasker(smoothing_fwhm=5, standardize=True)
img = masker.fit_transform(file, confounds=confounds)
```
It is also possible to fine-tune a subset of noise components and their parameters:
```python
from load_confounds import Confounds
confounds = Confounds(strategy=['high_pass', 'motion', 'global'], motion="full").load(file)
```
You can check our tutorial on MyBinder for more info [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SIMEXP/load_confounds/HEAD?filepath=demo%2Fload_confounds_demo.ipynb) 

## Noise components
The following noise components are supported. Check the docstring of `Confounds` for more info on the parameters for each type of noise. 
*  `motion` the motion parameters including 6 translation/rotation (`basic`), and optionally derivatives, squares, and squared derivatives (`full`).
*  `high_pass` basis of discrete cosines covering slow time drift frequency band.
*  `wm_csf` the average signal of white matter and cerebrospinal fluid masks (`basic`), and optionally derivatives, squares, and squared derivatives (`full`). 
*  `global`  the global signal (`basic`), and optionally derivatives, squares, and squared derivatives (`full`). 
*  `compcor` the results of a PCA applied on a mask based on either anatomy (`anat`), temporal variance (`temp`), or both (`combined`).
*  `ica_aroma` the results of an idependent component analysis (ICA) followed by identification of noise components. This can be implementing by incorporating ICA regressors (`basic`) or directly loading a denoised file (`full`).
*  `scrub` regressors coding for time frames with excessive motion, using threshold on frame displacement and standardized DVARS (`basic`) and suppressing short time windows using the (Power et al., 2014) appreach (`full`).

## Predefined strategies
The predefined strategies are all adapted from Ciric et al. 2017. Check the docstring of each strategy for more info and a list of parameters. 

| Strategy        | `high_pass` | `motion` | `wm_csf` | `global` | `compcor` | `ica_aroma` | `scrub` |
| --------------- |:-----------:|:--------:|:--------:|:--------:|:---------:|:-----------:|:-------:|
| `Params2`       | x           |          | `basic`  |          |           |             |         |
| `Params6`       | x           | `basic`  |          |          |           |             |         |
| `Params9`       | x           | `basic`  | `basic`  | `basic`  |           |             |         |
| `Params9Scrub`  | x           | `basic`  | `basic`  |          |           |             | `full`  |
| `Params24`      | x           | `full`   |          |          |           |             |         |
| `Params36`      | x           | `full`   | `full`   | `full`   |           |             |         |
| `Params36Scrub` | x           | `full`   | `full`   |          |           |             | `full`  |
| `AnatCompCor`   | x           | `full`   |          |          | `anat`    |             |         |
| `TempCompCor`   | x           |          |          |          | `temp`    |             |         |
| `ICAAROMA`      | x           |          | `basic`  |          |           | `full`      |         |
| `AROMAGSR`      | x           |          | `basic`  | `basic`  |           | `full`      |         |
| `AggrICAAROMA`  | x           |          | `basic`  | `basic`  |           | `basic`     |         |

## A note on nifti files and file collections
Note that if a `.nii.gz` file is specified, `load_confounds` will automatically look for the companion `tsv`confound file generated by fMRIprep. It is also possible to specify a list of confound (or imaging) files, in which case `load_confounds` will return a list of numpy ndarray.

## A note on low pass filtering
Low pass filtering is a common operation in resting-state fMRI analysis, and is featured in all preprocessing strategies of the Ciric et al. (2017) paper. fMRIprep does not output the discrete cosines for low pass filtering. Instead, this operation can be implemented directly with the nilearn masker, using the argument `low_pass`. Be sure to also specify the argument `tr` in the nilearn masker if you use `low_pass`.

## A note on high pass filtering and detrending 
Nilearn masker features two arguments to remove slow time drifts: `high_pass` and `detrend`. Both of these operations are redundant with the `high_pass` regressors generated by fMRIprep, and included in all `load_confounds` strategies. Do not use nilearn's `high_pass` or `detrend` options with these strategies. It is however possible to use a flexible `Confounds` loader to exclude the `high_pass` noise components, and then rely on nilearn's high pass filterning or detrending options. This is not advised with `compcor` or `ica_aroma` analysis, which have been generated with the `high_pass` components of fMRIprep. 

## A note on demeaning confounds
Unless you use the `detrend` or `high_pass` options of nilearn maskers, it may be important to demean the confounds. This is done by default by `load_confounds`, and is required to properly regress out confounds using nilearn with the `standardize=False`, `standardize=True` or `standardize="zscore"` options. If you want to use `standardize="psc"`, you will need to turn off the demeaning in `load_confounds`, which can be achieved using, e.g.:
```python
from load_confounds import Params6
conf = Params6(demean=False)
```

## A note on the choice of strategies 
We decided to focus our strategy catalogue on a reasonable but limited set of choices, and followed (mostly) the Ciric et al. (2017) reference. However, there are other strategies proposed in benchmarks such as (Parkes et al. 2018, Mascali et al. 2020).  Advanced users can still explore these other choices using the flexible `Confounds` API, which can be used to reproduce most denoising strategies in a single short and readable command.

## A note on denoising benchmarks 
There has been a number of benchmarks you may want to refer to in order to select a denoising strategy (e.g. Ciric et al., 2017, Parkes et al. 2018, Mascali et al., 2020). However, a number of caveats do apply and the conclusions of these studies may not directly apply to `load_confounds` strategies. First, the noise regressors generated by fMRIprep do not necessarily follow the same implementations as these papers did. For example, the way `load_confounds` implements scrubbing is by adding regressors, while Ciric et al. (2017) excluded outlier time points prior to regressing other confounds. There are also other aspects of the fMRI preprocessing pipelines which are not controlled by `load_confounds`. For example, Ciric et al. (2017) did apply image distortion correction in all preprocessing strategies. This step is controlled by fMRIprep, and cannot be changed through `load_confounds`. 

## Funding 
Development of this library was supported in part by the Canadian Consortium on Neurodegeneration in Aging ([CCNA](https://ccna-ccnv.ca/)) and in part by the Courtois Foundation. 

## References

Ciric R, Wolf DH, Power JD, Roalf DR, Baum GL, Ruparel K, Shinohara RT, Elliott MA, Eickhoff SB, Davatzikos C., Gur RC, Gur RE, Bassett DS, Satterthwaite TD. Benchmarking of participant-level confound regression strategies for the control of motion artifact in studies of functional connectivity. Neuroimage. 2017. doi:[10.1016/j.neuroimage.2017.03.020](https://doi.org/10.1016/j.neuroimage.2017.03.020)

Esteban O, Markiewicz CJ, Blair RW, Moodie CA, Isik AI, Erramuzpe A, Kent JD, Goncalves M, DuPre E, Snyder M, Oya H, Ghosh SS, Wright J, Durnez J, Poldrack RA, Gorgolewski KJ. fMRIPrep: a robust preprocessing pipeline for functional MRI. Nat Meth. 2018; doi: [10.1038/s41592-018-0235-4](https://doi.org/10.1038/s41592-018-0235-4)

Mascali, D, Moraschi, M, DiNuzzo, M, et al. Evaluation of denoising strategies for task‐based functional connectivity: Equalizing residual motion artifacts between rest and cognitively demanding tasks. Hum Brain Mapp. 2020; 1– 24. doi: [10.1002/hbm.25332](https://doi.org/10.1002/hbm.25332)

Parkes, L., Fulcher, B., Yucel, M., & Fornito, A. (2018). An evaluation of the efficacy, reliability, and sensitivity of motion correction strategies for resting-state functional MRI. NeuroImage, 171, 415-436. doi: [10.1016/j.neuroimage.2017.12.073](https://doi.org/10.1016/j.neuroimage.2017.12.073)

Power JD, Mitra A, Laumann TO, Snyder AZ, Schlaggar BL, Petersen SE. Methods to detect, characterize, and remove motion artifact in resting state fMRI. Neuroimage 2014 84:320-41. doi: [10.1016/j.neuroimage.2013.08.048](https://doi.org/10.1016/j.neuroimage.2013.08.048)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/FrancoisPgm"><img src="https://avatars.githubusercontent.com/u/35327799?v=4?s=100" width="100px;" alt=""/><br /><sub><b>François Paugam</b></sub></a><br /><a href="#infra-FrancoisPgm" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=FrancoisPgm" title="Code">💻</a> <a href="https://github.com/SIMEXP/load_confounds/pulls?q=is%3Apr+reviewed-by%3AFrancoisPgm" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=FrancoisPgm" title="Tests">⚠️</a> <a href="#data-FrancoisPgm" title="Data">🔣</a></td>
    <td align="center"><a href="https://github.com/HanadS"><img src="https://avatars.githubusercontent.com/u/26352860?v=4?s=100" width="100px;" alt=""/><br /><sub><b>HanadS</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/commits?author=HanadS" title="Code">💻</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=HanadS" title="Tests">⚠️</a> <a href="#data-HanadS" title="Data">🔣</a> <a href="#infra-HanadS" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=HanadS" title="Documentation">📖</a> <a href="#ideas-HanadS" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://emdupre.me"><img src="https://avatars.githubusercontent.com/u/15017191?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Elizabeth DuPre</b></sub></a><br /><a href="#ideas-emdupre" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://wanghaoting.com/"><img src="https://avatars.githubusercontent.com/u/13743617?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hao-Ting Wang</b></sub></a><br /><a href="#ideas-htwangtw" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=htwangtw" title="Code">💻</a> <a href="#data-htwangtw" title="Data">🔣</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=htwangtw" title="Documentation">📖</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=htwangtw" title="Tests">⚠️</a> <a href="https://github.com/SIMEXP/load_confounds/issues?q=author%3Ahtwangtw" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://simexp-lab.org"><img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pierre Bellec</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/commits?author=pbellec" title="Code">💻</a> <a href="https://github.com/SIMEXP/load_confounds/issues?q=author%3Apbellec" title="Bug reports">🐛</a> <a href="#ideas-pbellec" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-pbellec" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=pbellec" title="Tests">⚠️</a> <a href="#data-pbellec" title="Data">🔣</a> <a href="#eventOrganizing-pbellec" title="Event Organizing">📋</a> <a href="#maintenance-pbellec" title="Maintenance">🚧</a> <a href="#projectManagement-pbellec" title="Project Management">📆</a></td>
    <td align="center"><a href="https://scholar.harvard.edu/steven-meisler"><img src="https://avatars.githubusercontent.com/u/27028726?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Steven Meisler</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/issues?q=author%3Asmeisler" title="Bug reports">🐛</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=smeisler" title="Tests">⚠️</a> <a href="#data-smeisler" title="Data">🔣</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=smeisler" title="Code">💻</a> <a href="https://github.com/SIMEXP/load_confounds/commits?author=smeisler" title="Documentation">📖</a> <a href="#ideas-smeisler" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/effigies"><img src="https://avatars.githubusercontent.com/u/83442?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chris Markiewicz</b></sub></a><br /><a href="#ideas-effigies" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/srastegarnia"><img src="https://avatars.githubusercontent.com/u/64853244?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shima Rastegarnia</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/issues?q=author%3Asrastegarnia" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/nuKs"><img src="https://avatars.githubusercontent.com/u/1691962?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thibault PIRONT</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/commits?author=nuKs" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/m-w-w"><img src="https://avatars.githubusercontent.com/u/36826334?v=4?s=100" width="100px;" alt=""/><br /><sub><b>m-w-w</b></sub></a><br /><a href="https://github.com/SIMEXP/load_confounds/commits?author=m-w-w" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
