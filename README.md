# Sabd CLI

Because:

1. I need Gurbani on bash
2. I need to learn Python
3. We need something cross platform without the [Chintz](http://en.wikipedia.org/wiki/Chintz)

This script is waaaay faster than anything else out there and should work great.

HTML output uses [Reveal.js](http://lab.hakim.se/reveal-js/) which is way nicer than some of the STTM ppt output.  The application will fire up your web browser when in html mode

## Basic Usage
  `sabd-cli.py -f hjkk` to find "har jio kirpa karo" using first letter search

  `sabd-cli.py -s 2289` to bring all lines of "har jio kirpa karo" back

  `sabd-cli.py -s 2289 -o html` to bring all lines of "har jio kirpa karo" and render as html to a generated filename

  `sabd-cli.py -s 2289 -o html --file-name=/tmp/myfile.html` to bring all lines of "har jio kirpa karo" and render as html to a filename of your choice

  `sabd-cli.py (-h | --help)`


## TODO

- generate output helpers for openoffice presenter format
- use different gurbani databases such as GurbaniCD and SikhiToTheMax
- have unicode gurmukhi output
- wrap for windows and OSx
- have some front end wizzards work on the outputs
- create an interactive sabad picker

## Screenshots

### Searching for gurbani
![](https://github.com/jujhars13/sabd-cli/blob/master/screenshot-search.png?raw=true)

### HTML output
![](https://github.com/jujhars13/sabd-cli/blob/master/screenshot-html-output.png?raw=true)

## Requirements

- Python 2.7

### Ubuntu/Fedora
run `sudo pip install -r requirements.txt` to install all deps required for this project

## Tests
Run `nosetests` in the project root to run the unit tests

## License
See the LICENSE file for license rights and limitations (MIT) for the source code.
The databases may have their own separate license rights and limitations.


# BGG