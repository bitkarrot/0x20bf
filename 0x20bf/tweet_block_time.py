#!/usr/bin/env python3
from TwitterAPI import TwitterAPI

from logger import logger
from time_functions import btc_time, btc_unix_time_millis
from twitter_api_keys import AT, ATS, CAK, CASK, tweet

if tweet:
    api = TwitterAPI(CAK, CASK, AT, ATS)
    # if (LOGGER): print(api)


def set_old_block_time():
    f = open("OLD_BLOCK_TIME", "a+")
    f.write(str(btc_time()))
    f.close()


def get_old_block_time():
    f = open("OLD_BLOCK_TIME", "a+")
    OBT = str(f.read())
    f.close()
    # if DATA_LOGGER:
    # logger.info(OBT)  # unsecure
    set_old_block_time()
    return OBT


def tweet_block_time():
    # print(btc_time())
    # print(get_old_block_time())
    # print(int(btc_time()) != int(get_old_block_time()))
    # set_old_block_time()
    # if int(btc_time()) != int(get_old_block_time()):
    if tweet:
        request = api.request("statuses/update", {"status": btc_unix_time_millis()})
        # if LOGGER:
        # logger.info(request)
        if request.status_code == 200:
            logger.info("api.request SUCCESS")
        else:
            logger.info("api.request FAILURE")
        # else:
        #  logger.info("tweetblock_time() FAILURE")


if __name__ == "__main__":

    tweet_block_time()
