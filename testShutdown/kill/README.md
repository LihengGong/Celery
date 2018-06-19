# Celery shutdown test code
Celery Configuration tests

## Graceful shutdown

`app.control.broadcast('shutdown')`
will directly kill the worker from shell.




## How to run the test

### Start the worker in one shell in the directory of source code:

`worker -A tasks -Q tasksQA --loglevel=info -n W1`


### Start the tasks in another shell:

`./run_all.sh`

### While the tasks are running, kill the worker directly:

`pkill -9 -f 'celery'`

Then the worker will stop.

If the worker is started again, the tasks will resume:

`celery worker -A tasks -Q tasksQA --loglevel=info -n W1`
