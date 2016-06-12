'''
 Config, bootstrapping, DI and that sort of stuff
'''
__author__ = 'jujhar'

import configparser
import logging
import os.path

#application path constant to root of project
APPLICATION_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO)

# create a file handler
handler = logging.FileHandler(os.path.join(APPLICATION_PATH, 'logs/application.log'))
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
# add the handlers to the logger
logger.addHandler(handler)

config = configparser.ConfigParser()
config.read(os.path.join(APPLICATION_PATH, 'application/config/config.ini'))
config.set('production', 'APPLICATION_PATH', APPLICATION_PATH)
