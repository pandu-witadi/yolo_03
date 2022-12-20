#
#
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic.typing import List
import uuid
import logging
from pydantic.typing import List
from celery.result import AsyncResult

from config.mq_main import celery_execute
from config.default import CF
from model.prediction import Prediction


router = APIRouter()


@router.post('/process')
async def process(files: List[UploadFile] = File(...)):
    tasks = []
    try:
        for file in files:
            d = {}
            try:
                name = str(uuid.uuid4()).split('-')[0]
                ext = file.filename.split('.')[-1]
                file_name = f'{CF.UPLOAD_FOLDER}/{name}.{ext}'
                with open(file_name, 'wb+') as f:
                    f.write(file.file.read())
                f.close()

                # start task prediction
                task_id = celery_execute.send_task(
                    name='predict_image',
                    kwargs={
                        'data': os.path.join(CF.APP_FOLDER, file_name)
                    }
                )
                # task_id = celery_execute.send_task(
                #     name='test_add',
                #     kwargs={
                #             's': 5,
                #             'a': 1,
                #             'b': 2.1
                #         }
                # )
                # print(str(task_id))

                d['task_id'] = str(task_id)
                d['status'] = 'PROCESSING'
                d['url_result'] = f'/api/yolo/result/{task_id}'
            except Exception as ex:
                logging.info(ex)
                d['task_id'] = str(task_id)
                d['status'] = 'ERROR'
                d['url_result'] = ''

            tasks.append(d)
        return JSONResponse(status_code=202, content=tasks)
    except Exception as ex:
        logging.info(ex)
        return JSONResponse(status_code=400, content=[])


@router.get('/result/{task_id}')
async def result(task_id: str):
    task = AsyncResult(task_id)

    # Task Not Ready
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': task.status, 'result': ''})

    # Task done: return the value
    task_result = task.get()
    result = task_result.get('result')

    return JSONResponse(status_code=200, content={'task_id': str(task_id), 'status': task_result.get('status'), 'result': result})


@router.get('/status/{task_id}', response_model=Prediction)
async def status(task_id: str):
    task = AsyncResult(task_id)
    return JSONResponse(status_code=200, content={'task_id': str(task_id), 'status': task.status, 'result': ''})
    
