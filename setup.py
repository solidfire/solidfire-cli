from __future__ import print_function
import sys
from codecs import open
import os

from setuptools import setup, find_packages

DESCRIPTION = "A python client and CLI for accessing the SolidFire API."

if os.path.exists('README.rst'):
    with open('README.rst', 'r', 'utf-8') as readme_file:
        LONG_DESCRIPTION = readme_file.read()
else:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name='solidfire-python',
    version='0.0.1',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='SolidFire, Inc.',
    author_email='john.griffith@solidfire.com',
    packages=find_packages(exclude=["solidfire.tests"]),
    license='MIT',
    zip_safe=False,
    url='http://github.com/j-griffith/solidfire-python',
    entry_points={
        'console_scripts': [
            'sfcli= solidfire.cli.cli:cli',
        ],
    },
    install_requires=[
        'six >= 1.7.0',
        'prettytable >= 0.7.0',
        'click >= 5',
        'requests >= 2.7.0',
        'prompt_toolkit',
    ],
    tests_require=[
        'mock',
        'nose2',
    ],
    keywords=['solidfire'],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2.7',
    ],
)
