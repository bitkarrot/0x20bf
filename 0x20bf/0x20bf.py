#!/usr/bin/env python3
import hashlib

from configs import OLD_BLOCK_TIME
import configparser
from logger import logger
from search_gpg_key import search_gpg_key
from time_functions import btc_time, unix_time_millis
from TwitterAPI import TwitterAPI

# REF: https://docs.python.org/3/library/configparser.html
config = configparser.ConfigParser()
config.read('configs.ini')
config.sections()
config.get('DEFAULTSECT', "", fallback=False)
config.get('LOGGERDEFAULTS', "", fallback=False)
config.get('USERDEFAULTS', "", fallback=False)


if config.getboolean('USERDEFAULTS', 'tweet'):
    twitter_api = configparser.ConfigParser()
    twitter_api.read('twitter.ini')
    twitter_api.sections()
    twitter_api.get('TWITTERAPI', "", fallback=0)
    AT = twitter_api.get('[TWITTERAPI]', 'access_token')
    ATS = twitter_api.get('[TWITTERAPI]', 'access_token_secret')
    CAK = twitter_api.get('[TWITTERAPI]', 'consumer_api_key')
    CASK = twitter_api.get('[TWITTERAPI]', 'consumer_api_secret_key')
    api = TwitterAPI(
        CAK,
        CASK,
        AT,
        ATS
    )


def DELIMITER_STRIPPER(string):
    # avoiding incorrect SHA256 hashes
    string.strip(":")
    string.strip(".")
    return string.strip(":")


def test_hash_lib():
    TEST_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert TEST_256.digest_size == pow(2, 5)
    assert TEST_256.block_size == pow(2, 6)
    assert (
        TEST_256.hexdigest()
        == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    return TEST_256.hexdigest()


def HEX_MESSAGE_TREE(recipient, sender):
    recipient = DELIMITER_STRIPPER(recipient)
    sender = DELIMITER_STRIPPER(sender)

    n_256 = hashlib.sha256()
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info("n_256:")
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())
    # empty string reserved for protocol
    assert n_256.hexdigest() == test_hash_lib()

    # SHA256() + GPGR
    n_256.update(bytes(recipient, "utf-8"))
    # if (hex_logger): logger.info(n_256.digest())
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info("n_256 + recipient:")
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # SHA256() + GPGR+GPGS
    n_256.update(bytes(sender, "utf-8"))
    # if (hex_logger): logger.info(n_256.digest())
    # if (hex_logger): logger.info(n_256.hexdigest())
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info("n_256 + recipient+sender:")
        logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # TODO: populate message tree
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())

    return n_256.hexdigest()


def HEX_MESSAGE_DIGEST(recipient, message, sender):
    recipient = DELIMITER_STRIPPER(recipient)
    message = DELIMITER_STRIPPER(message)
    sender = DELIMITER_STRIPPER(sender)

    n_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert n_256.hexdigest() == test_hash_lib()

    # if (hex_logger): logger.info("%s",n_256.digest())
    # if (hex_logger): logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # SHA256() + GPGR
    n_256.update(bytes(recipient, "utf-8"))
    # if (hex_logger): logger.info(n_256.digest())
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # SHA256() + GPGR+MESSAGE
    n_256.update(bytes(message, "utf-8"))
    # if (hex_logger): logger.info(n_256.digest())
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # SHA256() + GPGR+MESSAGE+GPGS
    n_256.update(bytes(sender, "utf-8"))
    # if (hex_logger): logger.info(n_256.digest())
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())
    # if (hex_logger): logger.info(n_256.digest_size)
    # if (hex_logger): logger.info(n_256.block_size)

    # TODO: populate message tree
    if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
        logger.info(n_256.hexdigest())

    return n_256.hexdigest()


def message_header():
    # the HEADER is prepended with GPGR
    # the HEADER is appended with GPGS
    DIGEST = HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS)
    LOC = (
        "https://github.com/0x20bf-org/0x20bf/blob/main/"
        + GPGR
        + DIGEST
        + btc_time()
        + unix_time_millis()
        + GPGS
        + ".txt.gpg"
    )
    # LOC is appended on to DIGEST
    HEADER = str(
        ":"
        + GPGR
        + ":"
        + DIGEST
        + ":"
        + btc_time()
        + ":"
        + unix_time_millis()
        + ":"
        + GPGS
        + ":"
        + LOC
        + ":"
    )

    if config.getboolean('LOGGERDEFAULTS', 'logger'):
        logger.info(HEADER)
    # HEADER_STRUCTURE = str(":GPGR:DIGEST:btc_time:unix_time_millis:GPGS:LOC:")
    return HEADER


def send_message():
    header = message_header()
    # body = message_body()
    if config.getboolean('LOGGERDEFAULTS', 'logger'):
        logger.info(header)
    if btc_time() != OLD_BLOCK_TIME:
        if tweet:
            request = api.request("statuses/update", {"status": header})
            if request.status_code == 200:
                logger.info("api.request SUCCESS")
            else:
                logger.info("api.request FAILURE")
        else:
            logger.info("tweet=" + str(tweet))
    else:
        logger.info("tweetblock_time() FAILURE")


# logger.info(BTC_unix_time_millis())

GPGR = "4DC9817F"  # bitkarrot
logger.info(GPGR)
GPGS = "BB06757B"  # randymcmillan
logger.info(GPGS)
MESSAGE = "text human readable message"
if config.getboolean('LOGGERDEFAULTS', 'hex_logger'):
    logger.info(HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS))
HEX_MESSAGE_TREE(GPGR, GPGS)
HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS)

if config.getboolean('USERDEFAULTS', 'tweet'):
    send_message()
if config.getboolean('USERDEFAULTS', 'tweet'):
    search_gpg_key(GPGR)
    search_gpg_key(GPGS)
