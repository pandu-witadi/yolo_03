#
#
from typing import List

from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    REDIS_HOST: str = config('REDIS_HOST', default="localhost", cast=str)
    REDIS_PORT: str = config('REDIS_PORT', default="6379", cast=str)
    REDIS_DB: str = config('REDIS_DB', default="0", cast=str)
    REDIS_PASSWORD: str = config('REDIS_PASSWORD', default="", cast=str)

    BACKEND_URI: str = config('BACKEND_URI', default="redis://{host}:{port}".format(host=REDIS_HOST, port=REDIS_PORT), cast=str)
    BROKER_URI: str = config('BROKER_URI', default="amqp://192.168.88.18:5672", cast=str)

    DIR_OUTPUT: str = config('DIR_OUTPUT', default="/ml_api/static/results", cast=str)

    class Config:
        case_sensitive = True

CF = Settings()
