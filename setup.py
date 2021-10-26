"""Setup"""
from setuptools import setup, find_packages

setup(
    name=="fse",
    version="1.1",
    packages=find_packages(),
    install_requires=[
	"numpy~=1.21.2",
	"torch~=1.10.0",
	"pymesh~=1.0.2",
	"matplotlib~=3.4.2",
	"PyYAML~=6.0",
	"requests~=2.25.1"])