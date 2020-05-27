#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Usage:
        nluanalyzer -h|--help
        nluanalyzer -v|--version
        nluanalyzer <path>

    Options:
        -h --help                       Show this screen.
        -v --version                    Show version.
"""

__author__ = "Alvaro Arranz"
__copyright__ = "Copyright 2020, Alvaro Arranz"


import os
import sys
import docopt

from nluanalyzer import __version__
from nluanalyzer.converter import NLUAnalyzer


def init(args):
    if args['<path>']:
        input_path = args.get('<path>')
    else:
        input_path = os.path.abspath(os.curdir) + "/"

    nluanalyzer = NLUAnalyzer(input_path)

    nluanalyzer.__execute__()


def main():
    args = docopt.docopt(__doc__, version=__version__, options_first=True)

    try:
        init(args)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
