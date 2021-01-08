from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="load_confounds",
    version="0.6.5",
    description="load fMRIprep confounds in python",
    license="MIT",
    url="https://github.com/simexp/load_confounds",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Optional (see note above)
    project_urls={  # Optional
        "Bug Reports": "https://github.com/simexp/load_confounds/issues",
        "Funding": "https://cneuromod.ca",
        "Source": "https://github.com/simexp/load_confounds",
    },
    maintainer="Pierre Bellec",
    maintainer_email="pierre.bellec@gmail.com",
    packages=find_packages(),
    package_data={"load_confounds.data": ["*.nii.gz", "*.tsv"]},
    install_requires=[
        "numpy>=1.17.4",
        "pandas>=0.25.3",
        "scikit-learn>=0.21.3",
        "scipy>=1.3.2",
        "nilearn>=0.6.2",
    ],  # external packages as dependencies
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.5",
)
