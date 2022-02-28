#!/usr/bin/env python3
# from configs import HEX_LOGGER
from twitter_api_keys import CAK, CASK, AT, ATS
from TwitterAPI import TwitterAPI
from logger import logger
from time_functions import BTC_UNIX_TIME_MILLIS
# from hex_message_digest import HEX_MESSAGE_DIGEST

api = TwitterAPI(CAK, CASK, AT, ATS)


def search_gpgr(GPGR):
    # TODO: refactor asyncio
    try:
        global r
        request = api.request('search/tweets', {'q': GPGR})
        try:
            with open(GPGR + ":" + BTC_UNIX_TIME_MILLIS(), 'w+') as f:
                f.write(request.text)
                f.close
        except Exception:
            logger.info("TRY GPGR FAILED!")
            pass
    except Exception:
        logger.info("GPGR SEARCH FAILED!")
        pass


# GPGR = '4DC9817F'  # bitkarrot
# search_gpgr(GPGR)
# logger.info(GPGR)
