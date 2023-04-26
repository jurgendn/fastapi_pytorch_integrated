import os

from fastapi import FastAPI
from fastapi.responses import Response

from components.middlewares.validation import AuthorizedHeaderTokenMiddleware
from interfaces.responses import HELLO_WORLD
from routers import item

app = FastAPI()

app.add_middleware(middleware_class=AuthorizedHeaderTokenMiddleware,
                   secret_token=os.environ['SECRET_TOKEN'])
app.include_router(item.router)


@app.get("/")
async def index() -> Response:
    return HELLO_WORLD
