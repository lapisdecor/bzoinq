#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pyaudio"
]

test_requirements = [
    "pyaudio"
]

setup(
    name='bzoinq',
    version='0.1.4',
    description="Simple calendar alarms",
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
