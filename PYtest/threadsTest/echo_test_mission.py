import asyncio
import sys

HOST, PORT = "127.0.0.1", 7777
time = 2
mess = CASES = [b"hello\n", b"foo bar baz\n", b"\x00\x01\x02\n"]


async def message_Send(send: bytes):
    reader, writer = await asyncio.wait_for(
        asyncio.open_connection(HOST, PORT), timeout=time
    )
    try:
        writer.write(send)
        await writer.drain()
        get = await asyncio.wait_for(reader.read(4096), timeout=time)
        if get != send:
            print("失败")
            print(f"send{send!r}")
            print(f"get{get!r}")
            sys.exit(1)
        print(f"pass", send)
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    for m in mess:
        await message_Send(m)
    print("ok")


if __name__ == "__main__":
    asyncio.run(main())
