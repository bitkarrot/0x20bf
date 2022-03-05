#!/usr/bin/env python3
import os
import configparser

import psutil
from logger import logger

global user
global is_macos
global is_linux
global is_windows
user = psutil.Process().username()
is_macos = psutil.MACOS
is_linux = psutil.LINUX
# windows support not planned - but PRs are welcome
is_windows = psutil.WINDOWS

# Setup logging
global logger
global os_logger
global data_logger
global hex_logger
global genesis_time
global time_logger
global mempool_logger

# time_function data
# TODO: refactor for lower case and elsewhere
global BLOCK_TIP_HEIGHT
BLOCK_TIP_HEIGHT = os.path.expanduser(os.getcwd() + "/BLOCK_TIP_HEIGHT")
global DIFFICULTY
DIFFICULTY = os.path.expanduser(os.getcwd() + "/DIFFICULTY")
global BLOCK_TIME
BLOCK_TIME = os.path.expanduser(os.getcwd() + "/BLOCK_TIME")
global OLD_BLOCK_TIME
OLD_BLOCK_TIME = os.path.expanduser(os.getcwd() + "/OLD_BLOCK_TIME")

# global variables
# TODO: refactor for lower case and elsewhere
# we leave comments in PROTOCOL format ie. GPGR DIGEST etc...
global HEADER
global DIGEST
global BODY
global DATA
global TEST_256
global GPGR
global GPGS
global MESSAGE
global GOLDEN_RATIO

global tweet

# REF: https://docs.python.org/3/library/configparser.html
config = configparser.ConfigParser()
config.read('configs.ini')
config.sections()
config.get('DEFAULTSECT', "", fallback=False)
config.get('LOGGERDEFAULTS', "", fallback=False)
config.get('USERDEFAULTS', "", fallback=False)

if is_macos:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("is_macos"))

if is_linux:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("is_linux"))

if is_windows:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("is_windows"))

for key in config['DEFAULTSECT']:
    logger.info(key)
for key in config['LOGGERDEFAULTS']:
    logger.info(key)
for key in config['USERDEFAULTS']:
    logger.info(key)
