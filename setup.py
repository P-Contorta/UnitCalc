import os
import setuptools

def get_long_description()->str:
    with open("README.md","r") as f_handle:
        return f_handle.read()

setuptools.setup(
    name="UnitCalc",
    version="1.0.0",
    author="Nicholas Armstrong",
    author_email="nkarmstrong@ucdavis.edu",
    description="A Python Library for doing Scientific/Engineering mathematics!",
    long_description=get_long_description(),
    url="https://github.com/P-Contorta/UnitCalc",
    packages=setuptools.find_namespace_packages(),
    install_requires=[],
    include_package_data=True,
    keywords = ['Python3+',"GNU GPL 3.0 License",
                'SI','units',
                'Science',"Math","Engineering","Education","STEM"]
)