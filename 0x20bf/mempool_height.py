#!/usr/bin/env python3
import asyncio

import aiohttp
from configs import MEMPOOL_LOGGER, logger


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def mempool_height():
    async with aiohttp.ClientSession() as session:
        url = "https://mempool.space/api/blocks/tip/height"
        height = await fetch(session, url)
        if MEMPOOL_LOGGER:
            logger.info(height)
        return height


loop = asyncio.new_event_loop()
# loop = asyncio.get_event_loop()
loop.run_until_complete(mempool_height())
