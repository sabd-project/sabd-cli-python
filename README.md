# Sabd CLI

Because:

    1. I need Gurbani on bash
    2. I need to learn Python

## Basic Usage
  `sabd-cli -f hjkk` to find "har jio kirpa karo" using first letter search

  `sabd-cli -s 2289` to bring all lines of "har jio kirpa karo" back

  `sabd-cli -s 2289 -o html` to bring all lines of "har jio kirpa karo" and render as html

  `sabd-cli -s 2289 -o html` to bring all lines of "har jio kirpa karo" and render as html

  `sabd-cli (-h | --help)`


## TODO

- generate output helpers for openoffice presenter format
- use different gurbani databases such as GurbaniCD and SikhiToTheMax
- have unicode gurmukhi output
- wrap for windows and OSx
- have some front end wizzards work on the outputs
- create an interactive sabad picker

## Requirements

### Ubuntu/Fedora
run `sudo pip install -r requirements.txt` to install all deps required for this project

## Tests
Run `nosetests` in the project root to run the unit tests

## License
See the LICENSE file for license rights and limitations (MIT) for the source code.
The databases may have their own separate license rights and limitations.


# BGG