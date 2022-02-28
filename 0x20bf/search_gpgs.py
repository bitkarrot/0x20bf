#!/usr/bin/env python3
from configs import TWEET
from twitter_api_keys import CAK, CASK, AT, ATS
from TwitterAPI import TwitterAPI
from logger import logger
from time_functions import BTC_UNIX_TIME_MILLIS
# from hex_message_digest import HEX_MESSAGE_DIGEST


if (TWEET):
    api = TwitterAPI(CAK, CASK, AT, ATS)


def search_gpgs(GPGS):
    # TODO: refactor asyncio
    try:
        global r
        request = api.request('search/tweets', {'q': GPGS})
        try:
            with open(GPGS + ":" + BTC_UNIX_TIME_MILLIS(), 'w+') as f:
                f.write(request.text)
                f.close
        except Exception:
            logger.info("TRY GPGR FAILED!")
            pass
    except Exception:
        logger.info("GPGR SEARCH FAILED!")
        pass


GPGS = 'BB06757B'  # randymcmillan
search_gpgs(GPGS)
# logger.info(GPGS)
