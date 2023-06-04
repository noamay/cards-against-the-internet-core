from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from main import app


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())

