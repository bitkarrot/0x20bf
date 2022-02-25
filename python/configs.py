#!/usr/bin/env python3

from imports    import *

USER       = psutil.Process().username()
IS_MACOS   = psutil.MACOS
IS_LINUX   = psutil.LINUX
IS_WINDOWS = psutil.WINDOWS
# Setup logging
global LOGGER
LOGGER = True
global MEMPOOL_LOGGER
MEMPOOL_LOGGER = True
global TWEET
TWEET = False
global CONFIG
CONFIG                  = str('twitter_access_tokens')
global BLOCK_TIP_HEIGHT
BLOCK_TIP_HEIGHT        = os.path.expanduser(os.getcwd()+'/BLOCK_TIP_HEIGHT')
global DIFFICULTY
DIFFICULTY              = os.path.expanduser(os.getcwd()+'/DIFFICULTY')
global OLD_BLOCK_TIME
OLD_BLOCK_TIME          = os.path.expanduser(os.getcwd()+'/OLD_BLOCK_TIME')
global ACCESS_TOKEN_SECRET
ACCESS_TOKEN_SECRET     = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/access_token_secret.txt')
global ACCESS_TOKEN
ACCESS_TOKEN            = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/access_token.txt')
global CONSUMER_API_KEY
CONSUMER_API_KEY        = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/consumer_api_key.txt')
global CONSUMER_API_SECRET_KEY
CONSUMER_API_SECRET_KEY = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/consumer_api_secret_key.txt')
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
global CAK
global CASK
global AT
global ATS
global OBT

if (IS_MACOS):
    print(str("IS_MACOS"))

if (IS_LINUX):
    print(str("IS_LINUX"))

if (IS_WINDOWS):
    print(str("IS_WINDOWS"))


def insertPath(PATH):
    sys.path.append(PATH)


def getData(filename):
    f = open(filename, "r+")
    DATA = str(f.read())
    f.close()
    # if (LOGGER): print(DATA) #unsecure
    return DATA


CAK  = getData(CONSUMER_API_KEY)
CASK = getData(CONSUMER_API_SECRET_KEY)
AT   = getData(ACCESS_TOKEN)
ATS  = getData(ACCESS_TOKEN_SECRET)
OBT  = getData(OLD_BLOCK_TIME)


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%j.%Y %I:%M:%S %p')
logger = logging.getLogger()
UTF8Writer = codecs.getwriter('utf-8')
# sys.stdout = UTF8Writer(sys.stdout)

POWMOD_GMP_SIZE = pow(2, 256)

START_TIME = TimestampMillisec64()
CAFFEINATE = 18600

if __name__ == "__main__":

    from imports import *
    import argparse
    parser = argparse.ArgumentParser('config')
    parser.add_argument("-arg1", action="store_true", help="-arg1 example")
    parser.add_argument("-arg2", action="store_true", help="-arg2 example")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()
    if args.verbose:
        logger.info("args.verbose = %s",args.verbose)
        sys_info(args)
        pass
    if args.quiet:
        logger.info("args.quiet = %s",args.quiet)
        pass
    if args.arg1:
        logger.info("args.arg1 = %s",args.arg1)
        pass
    if args.arg2:
        logger.info("args.arg2 = %s",args.arg2)
        pass

