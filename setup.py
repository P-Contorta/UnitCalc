import os
import setuptools

def get_long_description()->str:
    with open("README.md","r") as f_handle:
        return f_handle.read()

setuptools.setup(
    name = "UnitCalc",
    version = "1.0.3",
    author = "Nicholas Armstrong",
    author_email = "nkarmstrong@ucdavis.edu",
    description = "A Python Library for doing Scientific/Engineering mathematics!",
    long_description = get_long_description(),
    url = "https://github.com/P-Contorta/UnitCalc",
    packages = setuptools.find_namespace_packages(),
    install_requires = [],
    include_package_data = True,
    python_requires = '>=3.6',
    classifiers = ["Development Status :: 3 - Alpha",
                   "Intended Audience :: End Users/Desktop",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Natural Language :: English",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Topic :: Scientific/Engineering",
                   "Topic :: Scientific/Engineering :: Astronomy",
                   "Topic :: Scientific/Engineering :: Chemistry",
                   "Topic :: Scientific/Engineering :: Mathematics",
                   "Topic :: Scientific/Engineering :: Physics"]
    keywords = ['Python3+',"GNU GPL 3.0 License",
                'SI','units',
                'Science',"Math","Engineering","Education","STEM"]
)