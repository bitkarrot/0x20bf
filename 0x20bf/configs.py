#!/usr/bin/env python3
import argparse
import logging
import os
import psutil

parser = argparse.ArgumentParser()
parser.add_argument( '-log',
                     default='warning',
                     help='Provide logging level. Example --log debug, default=warning' )

args = parser.parse_args()

if args.log:
    level_config = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING} 
    log_level = level_config[parser.parse_args().log.upper()]
    logging.basicConfig(level=log_level, format="%(asctime)s %(message)s", datefmt="%j.%Y %I:%M:%S %p")
    msg = f'Logging now setup at {args.log.upper()}'
    logging.info(msg)

logger = logging.getLogger()


USER = psutil.Process().username()
IS_MACOS = psutil.MACOS
IS_LINUX = psutil.LINUX
IS_WINDOWS = psutil.WINDOWS

# Setup logging
global LOGGER
LOGGER = True
global OS_LOGGER
OS_LOGGER = False
global DATA_LOGGER
DATA_LOGGER = False
global HEX_LOGGER
HEX_LOGGER = True
global GENESIS_TIME
GENESIS_TIME = 1231006505
global TIME_LOGGER
TIME_LOGGER = True
global MEMPOOL_LOGGER
MEMPOOL_LOGGER = False

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
GOLDEN_RATIO = 1.6180339887498948482045868343656381177203091798057628621354486227

global TWEET
TWEET = False

if IS_MACOS:
    if OS_LOGGER:
        logger.info(str("IS_MACOS"))

if IS_LINUX:
    if OS_LOGGER:
        logger.info(str("IS_LINUX"))

if IS_WINDOWS:
    if OS_LOGGER:
        logger.info(str("IS_WINDOWS"))
