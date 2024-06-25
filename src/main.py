from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database.database import create_tables
from .routers.words import router as word_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    await create_tables()
    print("База готова к работе")
    yield

app = FastAPI(title="Languages Dictionary", lifespan=lifespan)

app.include_router(word_router)
