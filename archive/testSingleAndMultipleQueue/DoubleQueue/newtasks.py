from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange
import time

app = Celery('tasks', backend = 'rpc://', broker = 'pyamqp://')

app.conf.task_queues = [
    Queue('tasksQQuick', routing_key = 'tasksQuick',
          queue_arguments = {'x-max-priority': 10}),
    Queue('tasksQLong', routing_key = 'tasksLong',
          queue_arguments = {'x-max-priority': 10})
]

app.conf.task_routes = {
    'tasks.example_task1': {'queue': 'tasksQQuick'},
    'tasks.example_task2': {'queue': 'tasksQQuick'},
    'tasks.example_task3': {'queue': 'tasksQLong'},
    'tasks.example_task4': {'queue': 'tasksQLong'}
}

app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = True

num1 = 0
num2 = 0
num3 = 0
num4 = 0

SLEEPTIME_SHORT = 0.2
SLEEPTIME_LONG = 20

@app.task
def task0():
    global num1
    global SLEEPTIME_SHORT
    print('Start0: ' + str(num1) + ', Start0')
    time.sleep(SLEEPTIME_SHORT)
    print('End0: ' + str(num1) + ', End0.')
    num1 += 1

@app.task
def example_task1():
    global num1
    global SLEEPTIME_SHORT
    print('Start1: ' + str(num1) + ', Start1')
    time.sleep(SLEEPTIME_SHORT)
    print('End1: ' + str(num1) + ', End1.')
    num1 += 1

@app.task
def example_task2():
    global num2
    global SLEEPTIME_SHORT
    print('Start2: ' + str(num2) + ', Start2')
    time.sleep(SLEEPTIME_SHORT)
    print('End2: ' + str(num2) + ', End2.')
    num2 += 1

@app.task
def example_task3():
    global num3
    global SLEEPTIME_LONG
    print('Start3: ' + str(num3) + ', Start3')
    time.sleep(SLEEPTIME_LONG)
    print('End3: ' + str(num3) + ', End3.')
    num3 += 1

@app.task
def example_task4():
    global num4
    global SLEEPTIME_LONG
    print('Start4: ' + str(num4) + ', Start4')
    time.sleep(SLEEPTIME_LONG)
    print('End4: ' + str(num4) + ', End4')
    num4 += 1
