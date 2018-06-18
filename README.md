# Celery
Celery Configuration tests

Various configurations are tested.

### Two configurations that need explanation:

```app.conf.worker_prefetch_multiplier = 1```

```app.conf.task_acks_late = True```

http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-worker_prefetch_multiplier

but the explanation is confusing

Refer to this link for a (relative) detailed explanation

https://stackoverflow.com/questions/16040039/understanding-celery-task-prefetching

## Priority

Conclusion: celery will honor priority as long as the tasks are submitted fast enough(i.e. at almost the same time).

| Tables        | Single Queue  | Double Queue  |
| ------------- |:-------------:|:-----:|
| Priority      | Yes           | Yes in both queues |


## Retry

Still working on the test code. Will update.