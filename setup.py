from setuptools import setup

setup(
   name='load_confounds',
   version='0.5.dev',
   description='load fMRIprep confounds in python',
   author='SIMEXP',
   packages=['.'],  #same as name
   author_email='arnaud.bore@gmail.com',
   install_requires=['numpy>=1.17.4', 'pandas>=0.25.3', 'scikit-learn>=0.21.3', 'scipy>=1.3.2', 'nilearn>=0.6.2'], #external packages as dependencies
)
