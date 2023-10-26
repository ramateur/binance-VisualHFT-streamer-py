import asyncio
import json
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync
from Exchange import UpdateSnapshot
from data_queue import put_to_queue_async, put_to_queue

async def task_BinanceLocalDepthCacheManager(exchange, market):
    #market = 'BTCUSDT'

    ubldc = BinanceLocalDepthCacheManager(exchange=exchange)
    # ubldc = BinanceLocalDepthCacheManager(exchange="binance.com-testnet")
    # ubldc = BinanceLocalDepthCacheManager(exchange="binance.com-futures")

    ubldc.create_depth_cache(markets=market)

    while True:
        await asyncio.sleep(0)
        #print(f"is_synchronized: {ubldc.is_depth_cache_synchronized(market)}")
        try:
            Snapshot = UpdateSnapshot(ubldc.get_asks(market=market)[:10], ubldc.get_bids(market=market)[:10], market)
            Market = {
                'data': json.dumps([Snapshot], default=str),
                'dataObj': [Snapshot],
                'type': 'Market'
                }
            await put_to_queue_async(json.dumps(Market, default=str))
        except DepthCacheOutOfSync as error_msg:
            print(f"ERROR: {error_msg}")
            await asyncio.sleep(1)