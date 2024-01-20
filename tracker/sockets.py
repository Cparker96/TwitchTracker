import websockets

async def init_socket():
    async with websockets.connect("wss://eventsub.wss.twitch.tv/ws") as websocket:
        await websocket.send("ping")
        message = await websocket.recv()
        return message