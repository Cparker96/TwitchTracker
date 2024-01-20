from auth import fetch_token
from sockets import init_socket
import asyncio

async def main():
    token = fetch_token()
    result = await init_socket()
    print(result)

asyncio.run(main())

