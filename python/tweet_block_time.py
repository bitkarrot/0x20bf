#!/usr/bin/env python3
from imports import *
from configs import *
from time_functions import *
api  = TwitterAPI(CAK,CASK,AT,ATS)
# if (LOGGER): print(api)

def tweet_block_time():
    if BTC_TIME() != OBT:
        request = api.request('statuses/update', {'status': BTC_UNIX_TIME_MILLIS()})
        if (LOGGER): logger.info(request)
        if (request.status_code == 200):
            logger.info('api.request SUCCESS')
        else:
            logger.info('api.request FAILURE')
    else:
        logger.info('tweetblock_time() FAILURE')

if __name__ == "__main__":

    from imports import *
    from configs import *
    tweet_block_time()
