#
#
import logging
from celery import Task
from celery.exceptions import MaxRetriesExceededError

from .index import app
from ml_celery.task.yolo import YoloModel

import time


class PredictTask(Task):
    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """ Load model on first call (i.e. first task processed) Avoids the need to load model on each task request """
        if not self.model:
            logging.info('Loading Model...')
            self.model = YoloModel()
            logging.info('Model loaded')
        return self.run(*args, **kwargs)


@app.task(
    ignore_result=False,
    bind=True,
    base=PredictTask,
    name='predict_image')
def predict_image(self, data):
    try:
        data_pred = self.model.predict(data)
        return {'status': 'SUCCESS', 'result': data_pred}
    except Exception as ex:
        try:
            self.retry(countdown=2)
        except MaxRetriesExceededError as ex:
            return {'status': 'FAIL', 'result': 'max retried achieved'}


@app.task(bind=True,
          name='test_add')
def test_add(self, s, a, b):
    time.sleep(s)
    return {'status': 'SUCCESS', 'result': a+b}
