from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange
import time

app = Celery('tasks', backend = 'rpc://', broker = 'pyamqp://')

app.conf.worker_prefetch_multiplier = 1
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
    'tasks.task_4': {'queue': 'tasksQA'}
}

SLEEPTIME = 0.01

@app.task
def task_1():
    global SLEEPTIME
    print('@@@@ task 1 before sleep @@@@')
    time.sleep(SLEEPTIME)
    print('@@@@ task 1 after sleep @@@@')

@app.task
def task_2():
    global SLEEPTIME
    print('@@@@ task 2 before sleep @@@@')
    time.sleep(SLEEPTIME)
    print('@@@@ task 2 after sleep @@@@')

@app.task
def task_3():
    global SLEEPTIME
    print('@@@@ task 3 before sleep @@@@')
    time.sleep(SLEEPTIME)
    print('@@@@ task 3 after sleep @@@@')

@app.task
def task_4():
    global SLEEPTIME
    print('@@@@ task 4 before sleep @@@@')
    time.sleep(SLEEPTIME)
    print('@@@@ task 4 after sleep @@@@')

#@app.task
#def task_5():
#    print('@@@@ task 5 before sleep @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 5 after sleep @@@@')
#
#@app.task
#def task_6():
#    print('@@@@ task 6 before sleep @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 6 after sleep @@@@')
#
#@app.task
#def task_7():
#    print('@@@@ task 7 before sleep @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 7 after sleep @@@@')
#
#@app.task
#def task_8():
#    print('@@@@ task 8 before sleep@@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 8 after sleep @@@@')
#
#@app.task
#def task_9():
#    print('@@@@ task 9 before @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 9 after @@@@')
#
#@app.task
#def task_10():
#    print('@@@@ task 10 before @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 10 after @@@@')
#
#@app.task
#def task_11():
#    print('@@@@ task 11 before @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 11 after @@@@')
#
#@app.task
#def task_12():
#    print('@@@@ task 12 before @@@@')
#    time.sleep(SLEEPTIME)
#    print('@@@@ task 12 after @@@@')