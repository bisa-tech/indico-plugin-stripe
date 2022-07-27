#!/usr/bin/env python
# -*- coding: utf-8 -*-



from setuptools import find_packages, setup

from indico_payment_stripe import __author__, __homepage__, __version__


with open('README.rst') as src:
    readme = src.read()
with open('CHANGELOG.rst') as src:
    changelog = src.read().replace('.. :changelog:', '')

with open('requirements.txt') as src:
    requirements = [line.strip() for line in src]
with open('requirements-dev.txt') as src:
    test_requirements = [line.strip() for line in src]

setup()
