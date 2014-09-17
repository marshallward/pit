"""pit.cli
   =======

   Command line interpreter module for pit

   :copyright: Copyright 2014 Aidan Heerdegen and Marshall Ward
   :license: Apache License, Version 2.0, see LICENSE for details
"""

# Standard Library
import argparse
import sys

# Local
from pit import __version__

def parse():
    """Parse command line inputs and execute the subcommand."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--version', action='version',
                        version='pit {}'.format(__version__))

    # TODO: Organise subcommands
    subparsers = parser.add_subparsers()

    # Display help if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        print(args)
