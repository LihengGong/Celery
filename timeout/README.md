# Set soft timeout to task

A single task can potentially run forever and if there are too many such tasks the worker will be jammed.

So it is a good practice to set a time limit to tasks.

There are two kinds of time limit:

+ **Soft limit**. The task will throw an exception(SoftTimeLimitExceeded) to allow itself to catch it and do the necessary clean up job before it is killed.

+ **Hard limit**. The hard timeout isn't catch-able and the task is forced to terminate.


## How to run the test code

+ In one shell:
`celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1`

(this command creates a worker named W1 which consumes from queue tasksQA and tasksQB)

+ In another shell:
`./run_all.sh`

We can see that `example_task1` will execute for 30 seconds(the soft time limit set in the code) before an exception is thrown.

## Some observations:
The task will be gone after it triggers the soft time limit and does the clean up.
