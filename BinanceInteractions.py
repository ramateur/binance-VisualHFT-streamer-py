import asyncio
import json
from Exchange import UpdateTrade
from data_queue import put_to_queue_async, put_to_queue
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
from secret import API_KEY, API_SECRET

HeartBeatBINANCE = {
                    'ProviderID': 23,
                    'ProviderName': 'Binance', 
                    'Status': 2
                    }

HeartBeats = {
            'data': json.dumps([HeartBeatBINANCE]),
            'dataObj': [HeartBeatBINANCE],
            'type': 'HeartBeats'
            }

heartbeats_js = json.dumps(HeartBeats)

async def task_listen_streams(market):
    def handle_socket_message(stream_data):
        #print(f"received data:\r\n{stream_data}\r\n")
        #put_to_queue(heartbeats_js)        
        if "trade" in json.dumps(stream_data):
            trade = UpdateTrade(json.loads(stream_data)['data'], market)
            Trade = {
                'data': json.dumps([trade], default=str),
                'dataObj': [trade],
                'type': 'Trades'
                }
            put_to_queue(json.dumps(Trade, default=str))
                

    ubwa = BinanceWebSocketApiManager(exchange='binance.com')
    api_stream = ubwa.create_stream(api=True, api_key=API_KEY, api_secret=API_SECRET,
                                    stream_label="Websocket API",
                                    process_stream_data=handle_socket_message)
    ubwa.create_stream(["trade"], market, process_stream_data=handle_socket_message)

    while True:                
        ubwa.api.ping(stream_id=api_stream)        
        await put_to_queue_async(heartbeats_js)
        await asyncio.sleep(5)