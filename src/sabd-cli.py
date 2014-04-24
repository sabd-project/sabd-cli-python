#!/use/bin/env python
# -*- coding: utf-8 -*-

'''sabd-cli

Because I need gurbani on the cli.

Usage: 
  sabd-cli [options] -f <query>
  sabd-cli (-h | --help)

Examples:
  sabd-cli -f hjkk <to find "har jio kirpa karo">

Options:
  -f <query>, --first-letter-search <query>     To do a first letter search
  -h, --help                                    Show this screen
'''

import docopt
import clint
import sqlite3
from models.isg_gurbani_db import Isg_gurbani_db

'''Main entry point for sabd-cli.'''


def main():
    args = docopt.docopt(__doc__, help=True, version=None, options_first=False)

    if (args['--first-letter-search']):
        print args['--first-letter-search']
        model_gurbani = Isg_gurbani_db()


if __name__ == '__main__':
    main()

