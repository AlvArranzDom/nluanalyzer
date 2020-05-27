===============================
``nluanalyzer``
===============================

Installation
------------

::

    pip install nluanalyzer

Usage
-----

::
    Usage:
        nluanalyzer -h|--help
        nluanalyzer -v|--version
        nluanalyzer <path>

    Options:
        -h --help                       Show this screen.
        -v --version                    Show version.
Example
-------

::

    $ nluanalyzer  intents.xlsx
    Successfully saved metrics file in /home/project/location/Formatted_Metrics.xlsx

Contents of requirements.txt

::

    wheel==0.23.0
    nltk==3.4.5
    spacy==2.2.4
    docopt==0.6.2
    numpy==1.17.4
    docopt==0.6.2
    pandas==0.25.3
    textacy==0.10.0
    scikit_learn==0.23.1