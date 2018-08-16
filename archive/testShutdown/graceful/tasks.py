from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange
import time

app = Celery('tasks', backend = 'rpc://', broker = 'pyamqp://')
SLEEPTIME = 2

app.conf.task_queues = [
    Queue('tasksQA', routing_key = 'tasksA',
          queue_arguments = {'x-max-priority': 10}),
    Queue('tasksQB', routing_key = 'tasksB',
          queue_arguments = {'x-max-priority': 10})
]

app.conf.task_routes = {
    'tasks.example_task1': {'queue': 'tasksQA'},
    'tasks.example_task2': {'queue': 'tasksQA'},
    'tasks.example_task3': {'queue': 'tasksQB'},
    'tasks.example_task4': {'queue': 'tasksQB'}
}

app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = True

num1 = 0
num2 = 0
num3 = 0
num4 = 0

@app.task
def example_task1():
    global num1
    global SLEEPTIME
    print('Start1: ' + str(num1) + ', Start1')
    time.sleep(SLEEPTIME)
    print('End1: ' + str(num1) + ', End1.')
    num1 += 1

@app.task
def example_task2():
    global num2
    global SLEEPTIME
    print('Start2: ' + str(num2) + ', Start2')
    time.sleep(SLEEPTIME)
    print('End2: ' + str(num2) + ', End2.')
    num2 += 1

@app.task
def example_task3():
    global num3
    global SLEEPTIME
    print('Start3: ' + str(num3) + ', Start3')
    time.sleep(SLEEPTIME)
    print('End3: ' + str(num3) + ', End3.')
    num3 += 1

@app.task
def example_task4():
    global num4
    global SLEEPTIME
    print('Start4: ' + str(num4) + ', Start4')
    time.sleep(SLEEPTIME)
    print('End4: ' + str(num4) + ', End4')
    num4 += 1
