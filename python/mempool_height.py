#!/usr/bin/env python3
from imports import *
from configs import *

import aiohttp
import asyncio

def request_blockcypher_height():
    global block_time
    global blockcypher_height
    try:
        # block_cypher = blockcypher.get_latest_blockcypher_height(coin_symbol='btc')
        block_cypher = blockcypher.get_latest_blockcypher_height()
        # logger.info(block_cypher)
        blockcypher_height = repr(block_cypher)
        f = open("BLOCK_TIME", "w")
        f.write("" + blockcypher_height + "\n")
        f.close()
        return blockcypher_height
    except:
        return 0
        pass

async def request_mempool_height():
    # curl -sSL "https://mempool.space/api/blocks/tip/height"
    url = "https://mempool.space/api/blocks/tip/height"
    if (MEMPOOL_LOGGER): logger.info(url)
    try:
        request = requests.get(url, stream=True)
    except:
        return 0
        pass
    return request.text

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def mempool_height():
    async with aiohttp.ClientSession() as session:
        url = "https://mempool.space/api/blocks/tip/height"
        height = await fetch(session, url)
        if (MEMPOOL_LOGGER): logger.info(height)
        return height

loop = asyncio.get_event_loop()
loop.run_until_complete(mempool_height())

