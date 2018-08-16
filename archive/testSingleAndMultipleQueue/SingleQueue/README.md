# Celery
Celery Configuration tests

## Problem with a single queue
https://www.vinta.com.br/blog/2018/dealing-resource-consuming-tasks-celery/

>If we have a task that takes too long to execute, then sharing the worker of quick tasks may cause a delay on the quick tasks execution and even resource starvation depending on the number of slow tasks.

In this test, there are two kinds of tasks, the first is quick tasks that can finish
in 0.2 seconds; the second is long tasks that takes as long as 20 seconds.

If these two kinds of tasks are mingled together in the same queue, the result is that the quick tasks are delayed considerably by the long tasks. 

## How to run the test

In shell in the directory of source code:

```celery worker -A tasks -Q tasksQA --loglevel=info -n W1```

In another shell:

```./runtasks.sh```