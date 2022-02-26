#!/usr/bin/env python3

import os
import sys
import time
import blockcypher
from mempool_height import *
import aiohttp
import asyncio

millis = int(round(time.time() * 1000))
seconds = int(round(time.time()))

try:
    block_time = blockcypher.get_latest_block_height(coin_symbol='btc')
    block_height = repr(block_time)
    f = open("BLOCK_TIME", "w")
    f.write("" + block_height + "\n")
    f.close()
    # print(block_time)
    # print(block_height)
except:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mempool_height())
    # logger.info(loop.run_until_complete(mempool_height()))
    block_height = loop.run_until_complete(mempool_height())
    f = open("BLOCK_TIME", "w")
    f.write("" + block_height + "\n")
    f.close()
    pass
# TODO: add more redundant block height checks