#!/usr/bin/env python3
import os
from logger     import *
import psutil
import codecs

USER       = psutil.Process().username()
IS_MACOS   = psutil.MACOS
IS_LINUX   = psutil.LINUX
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
global TIME_LOGGER
TIME_LOGGER = True
global MEMPOOL_LOGGER
MEMPOOL_LOGGER = True

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%j.%Y %I:%M:%S %p')
logger = logging.getLogger()
UTF8Writer = codecs.getwriter('utf-8')
# sys.stdout = UTF8Writer(sys.stdout)

# time_function data
global BLOCK_TIP_HEIGHT
BLOCK_TIP_HEIGHT        = os.path.expanduser(os.getcwd()+'/BLOCK_TIP_HEIGHT')
global DIFFICULTY
DIFFICULTY              = os.path.expanduser(os.getcwd()+'/DIFFICULTY')
global BLOCK_TIME
BLOCK_TIME              = os.path.expanduser(os.getcwd()+'/BLOCK_TIME')
global OLD_BLOCK_TIME
OLD_BLOCK_TIME          = os.path.expanduser(os.getcwd()+'/OLD_BLOCK_TIME')
global OBT

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

if (IS_MACOS):
    if (OS_LOGGER): print(str("IS_MACOS"))

if (IS_LINUX):
    if (OS_LOGGER): print(str("IS_LINUX"))

if (IS_WINDOWS):
    if (OS_LOGGER): print(str("IS_WINDOWS"))

if __name__ == "__main__":

    from imports import *
    from logger  import *

