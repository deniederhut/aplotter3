#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    desc = f.read()

setup(
    name='aplotter3',
    version='0.0.1',
    author="Imri Goldberg",
    packages=find_packages(),
    python_requires=">=3.5",
    long_description_content_type="text/markdown",
)
