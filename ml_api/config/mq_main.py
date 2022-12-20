#
#
from redis import Redis
from celery import Celery

from .default import CF

redis = Redis(
    host=CF.REDIS_HOST,
    port=CF.REDIS_PORT,
    password=CF.REDIS_PASSWORD,
    db=CF.REDIS_DB
)


celery_execute = Celery(
    broker=CF.BROKER_URI,
    backend=CF.BACKEND_URI
)
