#
#
from typing import List

from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = config('APP_NAME', default="ml-api__0.0.1", cast=str)
    HOST: str = config('HOST', default="0.0.0.0", cast=str)
    PORT: str = config('PORT', default=5152, cast=int)
    PATH_API: str = "/api"
    PATH_DOCS: str = "/api/docs"

    CORS_ORIGINS: List = [ "*" ]
    CORS_METHODS: List = [ "*" ]
    CORS_HEADERS: List = [ "*" ]
    CORS_CREDENTIAL: bool = True

    APP_FOLDER: str = config('APP_FOLDER', default="ml_api", cast=str)
    UPLOAD_FOLDER: str = config('UPLOAD_FOLDER', default="uploads", cast=str)
    STATIC_FOLDER: str = config('STATIC_FOLDER', default="static/results", cast=str)

    DEBUG_MODE: str = config("DEBUG_MODE", default=False, cast=bool)

    REDIS_HOST: str = config('REDIS_HOST', default="localhost", cast=str)
    REDIS_PORT: str = config('REDIS_PORT', default="6379", cast=str)
    REDIS_DB: str = config('REDIS_DB', default="0", cast=str)
    REDIS_PASSWORD: str = config('REDIS_PASSWORD', default="", cast=str)

    BACKEND_URI: str = config('BACKEND_URI', default="redis://{host}:{port}".format(host=REDIS_HOST, port=REDIS_PORT), cast=str)
    BROKER_URI: str = config('BROKER_URI', default="amqp://192.168.88.18:5672", cast=str)

    class Config:
        case_sensitive = True

CF = Settings()
