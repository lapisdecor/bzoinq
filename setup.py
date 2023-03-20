#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    name='bzoinq',
    version='0.1.5',
    description="Play a sound or run a function at some datetime",
    long_description=readme + '\n\n' + history,
    author="Luis Louro",
    author_email='lapisdecor@gmail.com',
    url='https://github.com/lapisdecor/bzoinq',
    packages=[
        'bzoinq',
    ],
    package_dir={'bzoinq':
                 'bzoinq'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='bzoinq',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
