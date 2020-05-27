#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from nluanalyzer import __version__
from setuptools.command.install import install as _install

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

import os
import nltk

lib_folder = os.path.dirname(os.path.realpath(__file__))

requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

os.system('python -m spacy download es')

nltk.download('stopwords')
nltk.download('spanish_grammars')

setup(
    name='nluanalizer',
    version=__version__,
    description='Natural Language Tool to Extract Features from Intents Dataset.',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author='Alvaro Arranz',
    author_email='alvaro.arranz@outlook.com',
    url='https://github.com/AlvArranzDom/nluanalyzer',
    keywords='nlu natural language spanish',
    packages=[
        'nluanalyzer',
    ],
    package_dir={
        'nluanalyzer': 'nluanalyzer'
    },
    setup_requires=install_requires,
    install_requires=install_requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'nluanalyzer=nluanalyzer.nluanalyzer:main',
        ],
    },
)
