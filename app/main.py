from app.core import config
from fastapi import FastAPI, Body, HTTPException
from pysentimiento import create_analyzer
from pysentimiento.analyzer import AnalyzerOutput
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.api.api import api_router
from app.containers import Container


container = Container()
container.init_resources()


app = FastAPI(
    openapi_url=f"{config.settings.API_V1_STR}/openapi.json",
    root_path=config.settings.ROOT_PATH,
    docs_url="/docs",
)

app.container = container

app.include_router(api_router, prefix=f'{config.settings.API_V1_STR}')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def skip_execution_if_warmup_call(func):
    def warmup_wrapper(event, context):
        print(str(event))
        if event.get("source") == "serverless-plugin-warmup":
            print("WarmUp - Lambda is warm!")
            return {}
        return func(event, context)
    return warmup_wrapper


@skip_execution_if_warmup_call
def handler(event, context):
    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)
    return response