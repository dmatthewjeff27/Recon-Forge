import aiohttp
import asyncio

class HttpClient:
    def __init__(self, timeout=5, user_agent="ReconForge/1.0"):
        self.timeout = timeout
        self.headers = {"User-Agent": user_agent}

    async def fetch(self, url):
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url, timeout=self.timeout) as resp:
                    return resp.status, await resp.text()
        except:
            return None, None
