#!/usr/bin/env python3
# Copyright 2015-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup


setup(
    name='wazo_auth-example-backend',
    version='0.0.1',

    description='A simple example backend plugin for wazo-auth',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'wazo_auth.backends': [
            'example = example_backend.example:ExampleBackend',
        ],
    }
)
