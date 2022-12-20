#
#
import os
import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from celery import Celery
from celery.result import AsyncResult

from config.default import CF
from config.mq_main import redis

from api.index import router


isdir = os.path.isdir(CF.UPLOAD_FOLDER)
if not isdir:
    os.makedirs(CF.UPLOAD_FOLDER)

isdir = os.path.isdir(CF.STATIC_FOLDER)
if not isdir:
    os.makedirs(CF.STATIC_FOLDER)

app = FastAPI(
    docs_url=CF.PATH_DOCS
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = CF.CORS_ORIGINS,
    allow_credentials = CF.CORS_CREDENTIAL,
    allow_methods = CF.CORS_METHODS,
    allow_headers = CF.CORS_HEADERS
)

app.mount("/static", StaticFiles(directory=CF.STATIC_FOLDER), name="static")

@app.on_event("startup")
async def startup_event():
    print(CF.APP_NAME + '  -  ' + CF.HOST + ':' + CF.PORT + ' startup ...')


@app.on_event("shutdown")
async def shutdown_event():
    print(CF.APP_NAME + '  -  ' + CF.HOST + ':' + CF.PORT + ' shutdown ...')

# --- route
app.include_router(router, prefix=CF.PATH_API)
