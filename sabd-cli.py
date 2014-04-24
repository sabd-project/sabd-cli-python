#!/use/bin/env python
# -*- coding: utf-8 -*-

'''sabd-cli

Because I need gurbani on the cli.

Usage: 
  sabd-cli [options] -f <query>
  sabd-cli [options] -s <sabd_id>
  sabd-cli (-h | --help)

Examples:
  sabd-cli -f hjkk <to find "har jio kirpa karo">
  sabd-cli -s 2289 <to bring all lines of "har jio kirpa karo" back>

Options:
  -f <query>, --first-letter-search <query>     To do a first letter search
  -s <sabad_id>, --sabd <sabad_id>              To bring a specific sabad back
  -h, --help                                    Show this screen
'''

import docopt
from clint.textui import colored

import application.bootstrap as bootstrap
from application.models.IsgGurbaniDb import IsgGurbaniDb


'''Main entry point for sabd-cli.'''


def main():
    args = docopt.docopt(__doc__, help=True, version=None, options_first=False)

    model_gurbani = IsgGurbaniDb(bootstrap.config)
    if args['--first-letter-search']:
        query = args['--first-letter-search'].strip()
        bootstrap.logger.info("Doing Gurmukhi first letter search with " + query)
        data = model_gurbani.first_letter_search(query)
        if data:
            print (getattr(colored, 'red')("sabd_id")) + "\t",
            print "Gurmukhi" + "\t"
            for line in data:
                print (getattr(colored, 'red')(line[0])) + "\t",
                print line[2] + "\t"



    # get a sabad
    if args['--sabd']:
        sabad_id = int(args['--sabd'])
        bootstrap.logger.info("getting sabad by id " + args['--sabd'])
        data = model_gurbani.get_sabad_by_sabad_id(sabad_id)
        if data:

            for line in data:
                #print (getattr(colored, 'cyan')(line[0])) + "\t", #ID
                #print (getattr(colored, 'cyan')(line[1])) + "\t", #ANG
                #print (getattr(colored, 'cyan')(line[2])) + "\t", #source
                #print (getattr(colored, 'cyan')(line[3])) + "\t", # line
                ##print (getattr(colored, 'red')(line[4])) + "\t", # sabd_id
                print line[5] + "\t"  # gurmukhi
                print line[6] + "\t"  #transliteration
                print (getattr(colored, 'cyan')(line[7])) + "\t"  #english translation
                print "\n"
                #print " " + (getattr(colored, 'magenta')line[1].ljust(40)


if __name__ == '__main__':
    main()

