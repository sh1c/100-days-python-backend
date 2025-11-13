#!/usr/bin/env python3


# 协程函数中获得实例前需要加await关键字,不然返回的是携程对象

import asyncio

HOST, PORT = "127.0.0.1", 7777
BUFSIZE = 1024


async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    add = writer.get_extra_info("peername")
    print(f"{add}正在连接")
    try:
        while True:
            data = await reader.read(BUFSIZE)
            if data == None:
                break
            writer.write(data)
            await writer.drain()

    except (ConnectionResetError, BrokenPipeError):
        pass

    finally:
        print(f"{add}已断开连接")
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(echo, HOST, PORT)
    print(f"服务器为{server.sockets[0].getsockname()}")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # 不加任何打印，直接正常结束
        pass
