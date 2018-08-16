# Celery priority test code
Celery Configuration tests

## Priority

Conclusion: celery will honor priority as long as the tasks are submitted fast enough.

If there are two queues, priority will be honored in each queue.

For task priority to take effect, tasks should be submitted fast enough at the same time so that worker has the chance
to sort these tasks according to their priority.


## How to run the test

### In one shell in the directory of source code:


One worker:
```celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1```

For two workers:

(both workers handle both queues)

```celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1```

```celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W2```

Or:

(each worker has a dedicated queue)

```celery worker -A tasks -Q tasksQA --loglevel=info -n W1```

```celery worker -A tasks -Q tasksQB --loglevel=info -n W1```

### In another shell:

```./run_all.sh```
