# Celery
Celery Configuration tests

Various configurations are tested.

***Caveat***: this code is only intended for study celery configurations.

Problems:

+ There is much redundant code.
+ Some arguments are hard-coded.

To-do:
Will restructure the code.

### Two configurations that need explanation:

```app.conf.worker_prefetch_multiplier = 1```

```app.conf.task_acks_late = True```

http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-worker_prefetch_multiplier

but the explanation is confusing

Refer to this link for a (relative) detailed explanation

https://stackoverflow.com/questions/16040039/understanding-celery-task-prefetching

Note that `prefetch count` is concept inherited from rabbitMQ. Please refer to this link for the concept of `prefetch count`:

https://mariuszwojcik.wordpress.com/2014/05/19/how-to-choose-prefetch-count-value-for-rabbitmq/


## Task Priority

Conclusion: celery will honor task priority as long as the tasks are submitted fast enough(i.e. at almost the same time), or put it more formally, if task priority is used, then the broker should be given enough time to "sort" the messages; if the tasks are very short, they will finish before the broker has enough time to "sort" them.

| Tables        | Single Queue  | Double Queue  |
| ------------- |:-------------:|:-----:|
| Priority      | Yes           | Yes in both queues |

However, task priority depends on the broker.

The following quote is comment from celery community.

https://github.com/celery/celery/issues/4819

> Task priority is tricky.
It is actually implemented by the broker.
If the tasks are short then the broker might not have enough time to sort the messages by priority.
So, in order to actually test priority you should try to run the worker with only one consumer thread and disable prefetching by using -Ofair.
Finally, try to queue the tasks and after that start the worker.
If there's nothing else in the queue you might not see priority sorting happening because of what goes on on the backend.

>It's usually recommended to use priority queues instead of broker priority weight. This way you group together any important tasks and give it more resources.

## Retry

Still working on the test code. Will update.

## Multiple Queues
