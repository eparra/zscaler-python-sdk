import httpx
from .config import ZscalerConfig

class ZscalerAsyncClient:
    """Async client using httpx."""

    def __init__(self, config: ZscalerConfig):
        self.config = config
        self._session = httpx.AsyncClient()

    async def close(self):
        await self._session.aclose()

    async def request(self, method: str, path: str, **kwargs):
        url = self.config.get_base_url().rstrip('/') + '/' + path.lstrip('/')
        headers = kwargs.pop('headers', {})
        headers['User-Agent'] = 'ZscalerSDK/2.0'
        resp = await self._session.request(method, url, headers=headers, **kwargs)
        resp.raise_for_status()
        return resp

    async def get(self, path: str, **kwargs):
        return await self.request('GET', path, **kwargs)

    async def post(self, path: str, json=None, **kwargs):
        return await self.request('POST', path, json=json, **kwargs)
