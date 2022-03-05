#!/usr/bin/env python3
import os
import configparser

import psutil
from logger import logger

USER = psutil.Process().username()
is_macos = psutil.MACOS
is_linux = psutil.LINUX
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
global BLOCK_TIP_HEIGHT
BLOCK_TIP_HEIGHT = os.path.expanduser(os.getcwd() + "/BLOCK_TIP_HEIGHT")
global DIFFICULTY
DIFFICULTY = os.path.expanduser(os.getcwd() + "/DIFFICULTY")
global BLOCK_TIME
BLOCK_TIME = os.path.expanduser(os.getcwd() + "/BLOCK_TIME")
global OLD_BLOCK_TIME
OLD_BLOCK_TIME = os.path.expanduser(os.getcwd() + "/OLD_BLOCK_TIME")

# global variables
global HEADER
global DIGEST
global BODY
global DATA
global TEST_256
global GPGR
global GPGS
global MESSAGE
global GOLDEN_RATIO

global TWEET

config = configparser.ConfigParser()
config.read('configs.ini')
config.sections()
config.get('DEFAULTSECT', "", fallback=False)
config.get('LOGGERDEFAULTS', "", fallback=False)

if is_macos:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("IS_MACOS"))

if is_linux:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("IS_LINUX"))

if is_windows:
    if config.getboolean('LOGGERDEFAULTS', 'os_logger'):
        logger.info(str("IS_WINDOWS"))

for key in config['DEFAULTSECT']:
    print(key)
for key in config['LOGGERDEFAULTS']:
    print(key)
for key in config['USERDEFAULTS']:
    print(key)
