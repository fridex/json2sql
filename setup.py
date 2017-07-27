#!/usr/bin/python3

import sys
from setuptools import setup


NAME = 'json2sql'


def get_requirements():
    with open('requirements.txt') as fd:
        return fd.read().splitlines()


if sys.version_info[0] != 3:
    sys.exit("Python3 is required in order to install %s" % NAME)

setup(
    name=NAME,
    version='0.0.0',
    packages=[NAME],
    install_requires=get_requirements(),
    author='Fridolin Pokorny',
    author_email='fridolin.pokorny@gmail.com',
    maintainer='Fridolin Pokorny',
    maintainer_email='fridolin.pokorny@gmail.com',
    description='convert JSON to raw SQL statement',
    url='https://github.com/fridex/json2sql',
    license='ASL 2.0',
    keywords='json sql tool converter',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
