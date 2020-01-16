from setuptools import setup

setup(
   name='load_confounds',
   version='0.1',
   description='load fMRIprep confounds in python',
   author='Hanad Sharmarke and collaborators',
   packages=['.'],  #same as name
   author_email='hanadsharmarke@gmail.com',
   install_requires=['numpy>=1.17.4', 'pandas>=0.25.3', 'scikit-learn>=0.21.3', 'scipy>=1.3.2'], #external packages as dependencies
)
