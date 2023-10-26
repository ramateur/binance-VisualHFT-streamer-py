
import asyncio

q = asyncio.Queue()
max_queue_size = 500

async def put_to_queue_async(data_json):
    await q.put(data_json)
    qsize = q.qsize()
    print(f'\rqueue size: {qsize:4}', end='')
    if(qsize > max_queue_size):        
        await q.get()

def put_to_queue(data_json):
    q.put_nowait(data_json)
    qsize = q.qsize()
    #print(f'queue size: {qsize}\r')
    if(qsize > max_queue_size):
        q.get_nowait()