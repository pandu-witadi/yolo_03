#
#
from celery import Celery

from ml_celery.config.init_broker import is_broker_running
from ml_celery.config.init_redis import is_backend_running
from ml_celery.config.default import CF


if not is_backend_running(CF.REDIS_HOST, CF.REDIS_PORT, CF.REDIS_DB, CF.REDIS_PASSWORD):
    exit()

if not is_broker_running(CF.BROKER_URI):
    exit()


app = Celery(
    'ml_celery',
    broker=CF.BROKER_URI,
    backend=CF.BACKEND_URI,
    include=['ml_celery.tasklist']
)
