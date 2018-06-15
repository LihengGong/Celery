# Celery
Celery Configuration tests

## Priority

Conclusion: celery will honor priority as long as the tasks are submitted fast enough.
If there are two queues, priority will be honored in each queue.

For task priority to take effect, tasks should be submitted fast enough at the same time so that worker has the chance
to sort these tasks according to their priority.


## How to run the test

In shell in the directory of source code:

```celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1```

In another shell:

```./run_all.sh```
