# Stop and Start Consuming from a Queue

Two APIs can be used to tell all(or specific) workers to stop or start
consuming from queue respectively:

+ [app name].control.cancel_consumer([queue name])

+ [app name].control.add_consumer([queue name])


## How to use

+ In one shell:
`celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1`

(this command creates a worker named W1 which consumes from queue tasksQA and tasksQB)

+ In another shell:
`python cancel_add.py`

+ In the third shell:
`./run_all.sh`

We can see that celery worker `W1` will stop consuming from `tasksQA` after receiving the
`cancel_consumer` call and will start consuming from `tasksQA` after receiving the `add_consumer`
call.


## Some observations
+ Start a worker, then tell the worker to stop consuming from a queue, then kill the worker and restart it, the worker will consuming from that queue again.
