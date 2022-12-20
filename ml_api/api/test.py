#
#
from fastapi import APIRouter
import time
from random import random

from config.default import CF


router = APIRouter()

@router.get('/')
async def test():
    return {
        "appName": CF.APP_NAME,
        "port": CF.PORT,
        "host": CF.HOST,
        "path_api": CF.PATH_API,
        "path_docs": CF.PATH_DOCS,
        "random": random(),
        "time": time.strftime("%a, %Y - %m - %d  %H:%M:%S")
    }
