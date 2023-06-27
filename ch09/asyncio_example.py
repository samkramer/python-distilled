# 9.15.1 asyncio Module
# https://docs.python.org/3/library/asyncio.html

import asyncio
import socket


async def echo_server(address):
    loop = asyncio.get_event_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    print('Server listening at', address)
    with sock:
        while True:
            client, addr = await loop.sock_accept(sock)
            print('Connection from', addr)
            loop.create_task(echo_client(loop, client))

			
async def echo_client(loop, client):
    with client:
        while True:
            data = await loop.sock_recv(client, 10000)
            if not data:
                break
            await loop.sock_sendall(client, b'Got:' + data)
    print('Connection closed')


# To test this code, use a program such as nc or telnet to connect 
# to port 25000 on your machine.
# The code should echo back the text that you type
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(echo_server(('', 25000)))
