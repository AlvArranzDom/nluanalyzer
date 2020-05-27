============
NLU Analyzer
============
---------------------------------------------------------------
Natural Language Tool to Extract Features from Intents Dataset.
---------------------------------------------------------------

Introduction
============

This package will help the user to extract ngrams, nouns, verbs,
adverbs and more features from an Intent Dataset in Spanish. This
will help the user to balance the dataset by comparing number of
ocurrences of each feature in each intent.

The entry format is an excel (.xlsx). Each column would be an intent
and in the first row it has to be informed the intent name, then
in the next rows the sentences for each intent training.

The output format is a json. It will have one dictionary per intent
including all the features extracted.

How to use it?
==============

Installation
------------
.. sourcecode::

    pip install nluanalyzer

Usage
-----
Usage

.. sourcecode::

    nluanalyzer -h|--help
    nluanalyzer -v|--version
    nluanalyzer <excel_path>


Options

.. sourcecode::

    -h --help                    Show help screen.
    -v --version                 Show version.

Example
-------
.. sourcecode::

    $ nlu_analyzer  intents.xlsx
    'Successfully saved intents analyzed file in /home/project/location/Formatted_Metrics.xlsx'

Package Requirements
====================

- nltk==3.4.5
- spacy==2.2.4
- docopt==0.6.2
- numpy==1.17.4
- docopt==0.6.2
- pandas==0.25.3
- textacy==0.10.0
- scikit_learn==0.23.1