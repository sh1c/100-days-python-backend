#!/usr/bin/env python3
import asyncio

HOST, PORT = "127.0.0.1", 7777
BUFSIZE = 1024


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"[+] {addr} connected")
    try:
        while data := await reader.read(BUFSIZE):
            writer.write(data)
            await writer.drain()
    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        print(f"[-] {addr} disconnected")
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    print(f"[*] Serving on {server.sockets[0].getsockname()}")
    async with server:  # 退出时自动 close/wait_closed
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())  # 一行启动事件循环
