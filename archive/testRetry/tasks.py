from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange
import time

app = Celery('tasks', backend = 'rpc://', broker = 'pyamqp://')

app.conf. worker_prefetch_multiplier = 1
app.conf.task_acks_late = True

app.conf.task_queues = [
    Queue('tasksQA', routing_key = 'tasksA',
          queue_arguments = {'x-max-priority': 10}),
    Queue('tasksQB', routing_key = 'tasksB',
          queue_arguments = {'x-max-priority': 10})
]

app.conf.task_routes = {
    'tasks.task_1': {'queue': 'tasksQA'},
    'tasks.task_2': {'queue': 'tasksQA'},
    'tasks.task_3': {'queue': 'tasksQA'},
    'tasks.task_4': {'queue': 'tasksQA'},
}

SLEEPTIME = 1
NUM1 = 0

@app.task(bind = True, default_retry_delay = 15)
def task_1(self):
    global SLEEPTIME
    global NUM1
    print('task 1 before exception')
    NUM1 += 1

    try:
        while NUM1 < 5:
            time.sleep(SLEEPTIME)
            print('throw exceptions')
            raise ValueError('Raised a ValueError')
        print('NUM1: ' + str(NUM1))
        time.sleep(SLEEPTIME)
    except(ValueError) as exc:
        raise self.retry(exc=exc)

    print('task 1 after exception')
