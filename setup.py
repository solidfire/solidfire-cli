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
    name='solidfire-cli',
    version='1.4.0.333',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='SolidFire, Inc.',
    author_email='ariel.hoffman@solidfire.com, adam.haid@solidfire.com',
    packages=find_packages(exclude=["element.tests"]),
    license='MIT',
    zip_safe=False,
    url='https://github.com/solidfire/Python-CLI/tree/release0.0',
    entry_points={
        'console_scripts': [
            'sfcli=element.cli.cli:cli',
        ],
    },
    install_requires=[
        'click >= 5',
		'future',
		'setuptools',
        'simplejson',
        'jsonpickle >= 0.9.3',
		'solidfire-sdk-python >= 1.2',
        'pycryptodome >= 2.6.1',
        'FileLock'
    ],
    tests_require=[
        'mock',
        'nose2',
    ],
    keywords=['element'],
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
