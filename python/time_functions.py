#!/usr/bin/env python3
from configs import *
import aiohttp
import asyncio
import os
import sys
import time
import math
import shutil
import blockcypher
from logger import *

from mempool_height import mempool_height

async def touch_time(time):
    f = open(os.getcwd()+"/BLOCK_TIME", "w")
    f.write("" + str(time) + "\n")
    f.close()

def move_block_time():
    try:
        shutil.move(os.getcwd()+"/BLOCK_TIME", os.getcwd()+"/OLD_BLOCK_TIME")
    except:
        logger.info("moveblock_time() failed!")
        touch_time()
        pass

def getMillis():
    global millis
    millis = int(round(time.time() * 1000))
    return millis

def getSeconds():
    global seconds
    seconds = int(round(time.time()))
    return seconds

def blockcypher_height():
    try:
        # block_cypher = blockcypher.get_latest_blockcypher_height(coin_symbol='btc')
        block_cypher = blockcypher.get_latest_blockcypher_height()
        blockcypher_height = repr(block_cypher)
        f = open("BLOCK_TIME", "w")
        f.write("" + blockcypher_height + "\n")
        f.close()
        return int(blockcypher_height)
    except:
        return 0
        pass

def BTC_TIME():
    mempool_loop = asyncio.new_event_loop()
    BTC_TIME = mempool_loop.run_until_complete(mempool_height())
    assert int(BTC_TIME) >= int(blockcypher_height())
    return int(BTC_TIME)

def BTC_UNIX_TIME_MILLIS():
    global btc_unix_time_millis
    global SESSION_ID
    btc_unix_time_millis = str(BTC_TIME())+":"+str(getMillis())
    SESSION_ID = btc_unix_time_millis
    f = open("SESSION_ID", "w")
    f.write("" + SESSION_ID + "\n")
    f.close()
    f = open("SESSION_ID.lock", "w")
    f.write("" + SESSION_ID + "\n")
    f.close()
    return btc_unix_time_millis

def BTC_UNIX_TIME_SECONDS():
    global btc_unix_time_seconds
    btc_unix_time_seconds = str(BTC_TIME())+":"+str(getSeconds())
    return btc_unix_time_seconds

def UNIX_TIME_MILLIS():
    global unix_time_millis
    unix_time_millis = str(getMillis())
    return unix_time_millis

def UNIX_TIME_SECONDS():
    global unix_time_seconds
    unix_time_seconds = str(getSeconds())
    return unix_time_seconds

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def mempool_height():
    async with aiohttp.ClientSession() as session:
        url = "https://mempool.space/api/blocks/tip/height"
        height = await fetch(session, url)
        if (MEMPOOL_LOGGER): logger.info(height)
        return height

loop = asyncio.new_event_loop()
loop.run_until_complete(touch_time(BTC_TIME()))
loop.run_until_complete(mempool_height())

