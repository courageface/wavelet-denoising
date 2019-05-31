from setuptools import setup
import os
from os import path

name = "wtdenoise"
description = "Wavelet denoising functions"
long_description = "Wavelet denoising functions, including baseline, threshold shrinkage denoising, translation invariant denoising. "

this_directory = path.abspath(path.dirname(__file__))


def read(filename):
    with open(os.path.join(this_directory, filename), "rb") as f:
        return f.read().decode("utf-8")


if os.path.exists("README.md"):
    long_description = read("README.md")

packages = ['wtdenoise']
url = "https://github.com/courageface/wavelet-denoising"
author = "Xie Xinyan"
author_email = "hsiehxy@outlook.com"
description = "Wavelet denoising functions"
classifiers = [
    'Development Status :: 3',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries :: Python Modules',
    "Topic :: Scientific/Engineering :: Signal Processing",
    'Intended Audience :: Science/Research',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Environment :: Console'
]

setup(
    name=name,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=author,
    url=url,
    author_email=author_email,
    classifiers=classifiers,
    install_requires=[
        "numpy",
        "PyWavelets==0.5.2",
    ],
    version='0.1.0',
    packages=packages
)
