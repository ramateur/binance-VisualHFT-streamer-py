import asyncio
from websockets.server import serve
from data_queue import q, put_to_queue

async def ws_data(websocket):
    while True:
        data_json = await q.get()
        await websocket.send(data_json)

async def task_ws_server(host, port):
    async with serve(ws_data, "localhost", 6900):
        await asyncio.Future()