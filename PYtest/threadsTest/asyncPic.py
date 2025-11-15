import asyncio
from pathlib import Path

import aiohttp

DOWN_DIR = Path("down_img")
DOWN_DIR.mkdir(exist_ok=True)

# 10 张示例图（可替换为自己的）
urls = [f"https://picsum.photos/200/300?image={i}" for i in range(10)]


async def download(
    session: aiohttp.ClientSession, url: str, sem: asyncio.Semaphore
) -> None:
    async with sem:  # 控制并发
        async with session.get(url) as resp:
            if resp.status == 200:
                name = url.split("/")[-1][4:] + ".jpg"
                (DOWN_DIR / name).write_bytes(await resp.read())
                print(f"{name} 下载完成")
            else:
                print(f"{url} 下载失败，状态码 {resp.status}")


async def main():
    sem = asyncio.Semaphore(10)  # 最多 10 并发
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download(session, u, sem)) for u in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
