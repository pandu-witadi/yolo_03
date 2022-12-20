#
#
from fastapi import APIRouter
from celery import Celery
from celery.result import AsyncResult

from api import test, yolo


router = APIRouter()

router.include_router(test.router, prefix="/test",  tags=["test"])
router.include_router(yolo.router, prefix="/yolo",  tags=["yolo"])
