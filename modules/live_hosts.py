import aiohttp
import asyncio

class LiveHostDetector:
    async def check(self, session, host):
        for scheme in ["http", "https"]:
            try:
                async with session.get(f"{scheme}://{host}", timeout=5) as r:
                    return host, r.status
            except:
                pass
        return None

    async def detect(self, hosts):
        live = {}
        async with aiohttp.ClientSession() as session:
            tasks = [self.check(session, h) for h in hosts]
            results = await asyncio.gather(*tasks)
            for r in results:
                if r:
                    live[r[0]] = r[1]
        return live
