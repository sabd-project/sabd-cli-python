# Sabd CLI

[![Build Status](https://travis-ci.org/jujhars13/sabd-cli.svg?branch=master)](https://travis-ci.org/jujhars13/sabd-cli)

Why? Because:

1. I need Gurbani on bash
2. I need to learn Python

This script is waaaay faster than anything else out there - bGg.

HTML output uses [Reveal.js](http://lab.hakim.se/reveal-js/) which is very nice, please fork and see if you can improve.

The application will fire up your web browser when in html mode so make sure you have a proper (*chrome*) one.

## Basic Usage
  `sabd-cli.py -f/q hjkk` to find "har jio kirpa karo" using first letter search

  `sabd-cli.py -s 2289` to bring all lines of "har jio kirpa karo" back

  `sabd-cli.py -s 2289 -o html` to bring all lines of "har jio kirpa karo" and render as html in [presentation](http://lab.hakim.se/reveal-js/) mode

  `sabd-cli.py -s 2289 -o html --html-type line-by-line ` to bring all lines of "har jio kirpa karo" and render as line-by-line html

  `sabd-cli.py (-h | --help)`

## Database
Currently we're using the [Search Gurbani](http://searchgurbani.com/sgdv/isg) database, might add other database support later

## TODO

- generate output helpers for libreoffice presenter format
- use different gurbani databases such as GurbaniCD and SikhiToTheMax
- have unicode gurmukhi output
- wrap for windows and OSx
- have some front end ninjas work on the html outputs
- create an interactive CLI based sabd picker
- create an installer
- create a HTML line navigator for the HTML view
- allow the switching of html output types
- implement other search types
- create a GUI???

## Screenshots

### Searching for gurbani
![](https://github.com/jujhars13/sabd-cli/blob/master/screenshot-search.png?raw=true)

### HTML output in presentation mode using Reveal.js
![](https://github.com/jujhars13/sabd-cli/blob/master/screenshot-html-output.png?raw=true)

### Keyboard shortcuts
- `o` will bring up reveal.js's built in slide overview view
- `i` will toggle in my dirty 20 min hacked Gurmukhi navigator

## Requirements

- Python 3.5

run `pip install -r requirements.txt` to install all deps required for this project

### Windows
You may need to set the `set PYTHONIOENCODING=utf-8` env variable for unicode to work on Windows console

## Tests
Using [nose](https://nose.readthedocs.org/en/latest/) as a test framework (see sabd id 51).

Run `nosetests` in the project root to run the unit tests

## License
See the LICENSE file for license rights and limitations (MIT) for the source code.
The databases may have their own separate license rights and limitations, youll have to speak to the owners

---
bGg
