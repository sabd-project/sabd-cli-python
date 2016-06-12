#!/usr/bin/python
# -*- coding: utf-8 -*-

'''sabd-cli

Because I need gurbani on the cli.

Usage:
  sabd-cli [options] -q <query>
  sabd-cli [options] -s <sabd_id>
  sabd-cli (-h | --help)

Examples:
  sabd-cli -q hjkk <to find "har jio kirpa karo">
  sabd-cli -s 2289 <to bring all lines of "har jio kirpa karo" back>

Options:
  -q <query>, --first-letter-search <query>     To do a first letter search
  -s <sabad_id>, --sabd <sabad_id>              To bring a specific sabd back
  -o, --output-as html|txt|md                   Output sabd as html|txt|md
  --html-template line-by-line|presentation     If html then output as line-by-line[default] mode or presentation
  -h, --help                                    Show this screen
'''

import docopt
from clint.textui import colored
import tempfile
# for html output
from jinja2 import Environment, PackageLoader
import webbrowser

import application.bootstrap as bootstrap
from application.models.IsgGurbaniDb import IsgGurbaniDb


def main():
    '''Main entry point for sabd-cli.'''
    args = docopt.docopt(__doc__, help=True, version=None, options_first=False)

    if args['--output-as'] and args['--output-as'] not in ['md', 'txt', 'html']:
        bootstrap.logger.info("we don't support that file format yet")
        quit()

    model_gurbani = IsgGurbaniDb(bootstrap.config)
    if args['--first-letter-search']:
        query = args['--first-letter-search'].strip()
        bootstrap.logger.info("Doing Gurmukhi first letter search with " + query)

        try:
            data = model_gurbani.first_letter_search(query)
        except Exception as e:
            bootstrap.logger.critical("There was an issue searching for " + query, e.message)

        if data:
            print (getattr(colored, 'yellow')("sabd_id") + " " + "Gurmukhi")
            print (getattr(colored, 'red')("----------------"))
            for line in data:
                print (getattr(colored, 'yellow')(line[1]) + " " + line[2] + "\t")

        else:
            bootstrap.logger.warn("couldn't find any sabds with first letter search: " + query)


    # get a sabad
    if args['--sabd']:
        sabd_id = int(args['--sabd'])
        bootstrap.logger.info("getting sabad by id " + str(sabd_id))
        bootstrap.logger.info("Searching for sabd by " + str(sabd_id))

        try:
            data = model_gurbani.get_sabad_by_sabad_id(sabd_id)
        except Exception as e:
            bootstrap.logger.critical("There was an issue searching for " + str(sabd_id), e.message)

        if data:
            if args['--output-as'] == 'txt':
                for line in data:
                    # print (getattr(colored, 'cyan')(line[0])) + "\t", #ID
                    #print (getattr(colored, 'cyan')(line[1])) + "\t", #ANG
                    #print (getattr(colored, 'cyan')(line[2])) + "\t", #source
                    #print (getattr(colored, 'cyan')(line[3])) + "\t", # line
                    ##print (getattr(colored, 'red')(line[4])) + "\t", # sabd_id
                    print (line[5])  # gurmukhi
                    print (line[6])  #transliteration
                    print (getattr(colored, 'cyan')(line[7]))  #english translation
                    print ("\n")
                    #print " " + (getattr(colored, 'magenta')line[1].ljust(40)
            elif args['--output-as'] == 'md':
                bootstrap.logger.warn("md output no yet implemented")
            else:  # default is presentation mode html
                html_mode = 'presentation'
                if args['--html-template']:
                    if args['--html-template'].strip() == 'line-by-line':
                        html_mode = 'line-by-line'

                output_file = tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix='.html', prefix='sabd-cli-', dir=None, delete=False)
                bootstrap.logger.info('output filename has not been specified, will write to ' + str(output_file.name))
                outputSabadAsFile(output_file, 'html', data, html_mode)

        else:
            bootstrap.logger.warn("couldn't find a sabad by " + str(sabd_id))


def outputSabadAsFile(file, type, data, html_template_type='line-by-line'):
    """
    Output sabd as certain filetypes
    @param file the file object
    @param string md|html|txt
    @param dictionary data
    @param string html template type
    """
    if type == 'md':
        for line in data:
            file.write("**" + line[5].encode("UTF-8") + "**" + "\n")
            file.write("*" + line[6].encode("UTF-8") + "*" + "\n")
            file.write(line[7].encode("UTF-8") + "\n")
            file.write("\n")
        file.flush()
        file.close()

    if type == 'html':
        # use jinja templates
        env = Environment(loader=PackageLoader('application', 'views'))
        template = env.get_template(html_template_type + '.html')
        template_data = {'title': 'Sabad CLI output [' + html_template_type + ']', 'gurbani': data}
        output = template.render(template_data)
        file.write(output.encode("UTF-8"))
        file.flush()
        file.close()
        webbrowser.open(file.name, 2)  #open file in new browser 2=new tab
        quit()

    if type == 'txt':
        for line in data:
            file.write(line[5].encode("UTF-8") + "\n")
            file.write(line[6].encode("UTF-8") + "\n")
            file.write(line[7].encode("UTF-8") + "\n")
            file.write("\n")
        file.flush()
        file.close()

    bootstrap.logger.info("Finished, Written output to " + file.name)


if __name__ == '__main__':
    main()
