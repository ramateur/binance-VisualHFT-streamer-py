import asyncio
import logging
import logging.handlers as handlers
import os
from LocalCacheManager import task_BinanceLocalDepthCacheManager
from ws_server import task_ws_server
from BinanceInteractions import task_listen_streams

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(level=logging.INFO,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

market = 'BTCUSDT'

async def main():
    task_connect = asyncio.create_task(
        task_BinanceLocalDepthCacheManager("binance.com", market))

    task_serve = asyncio.create_task(
        task_ws_server("localhost", 6900))
    
    task_listen = asyncio.create_task(
        task_listen_streams(market))

    await task_connect
    await task_serve
    await task_listen

asyncio.run(main())
