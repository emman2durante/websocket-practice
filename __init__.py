import asyncio
import datetime
import random
import websockets

async def chat(websocket, path):
    while True:
        msg = await websocket.recv()
        await websocket.send(msg)

start_server = websockets.serve(chat, "10.5.89.15", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()