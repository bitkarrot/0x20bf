#!/usr/bin/env python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="0x20bf",
    version="0.0.1",
    author="randymcmillan, bitkarrot",
    author_email="randy.lee.mcmillan@gmail.com, bitkarrot@bitcoin.org.hk",
    description=("0x20bf: This document proposes an Internet standards track protocol for transporting, broadcasting and syndication of messages over common internet communications channels. The distribution of all documents related to this proposal are unlimited and unencumbered by any LICENSE, but some are included anyway."),
    license="Apache License 2.0",
    keywords="",
    url="http://packages.python.org/0x20bf",
    packages=['0x20bf', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache License 2.0",
    ],
)
