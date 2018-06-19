# Celery shutdown test code
Celery Configuration tests

## Graceful shutdown

`app.control.broadcast('shutdown')`
will gracefully shutdown the worker remotely.




## How to run the test

### Start the worker in one shell in the directory of source code:

`worker -A tasks -Q tasksQA --loglevel=info -n W1`


### Start the tasks in another shell:

`./run_all.sh`

### While the tasks are running, stop the worker remotely:

`python shutdown.py`

Then the worker will stop.

Note that occasionally, python will throw an exception as below.
>Task handler raised error: WorkerLostError('Worker exited prematurely: exitcode 0.',)

If the worker is started again, the tasks will resume:

`celery worker -A tasks -Q tasksQA --loglevel=info -n W1`
