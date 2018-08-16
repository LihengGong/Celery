
# List active tasks

`celery -A tasks inspect active`


## How to run
+ In one shell:

`celery worker -A tasks -Q tasksQA,tasksQB --loglevel=info -n W1`

+ In another shell:

`./run_all`

+ In the third shell:

`celery -A tasks inspect active`


### When there are no active tasks:

*Output*:
 >celery@W1: OK
    - empty -

### When there are active tasks:

*Output*:
 >celery@W1: OK
    * {'id': 'bb91c277-f8e2-42a1-90f7-f91c8709e776', 'name': 'tasks.example_task1', 'args': '()', 'kwargs': '{}', 'type': 'tasks.example_task1', 'hostname': 'celery@W1', 'time_start': 1529444404.487525, 'acknowledged': False, 'delivery_info': {'exchange': '', 'routing_key': 'tasksQA', 'priority': 1, 'redelivered': False}, 'worker_pid': 42604}
    * {'id': '5d3d83e9-1eea-4977-9732-f9c11a42f1d1', 'name': 'tasks.example_task3', 'args': '()', 'kwargs': '{}', 'type': 'tasks.example_task3', 'hostname': 'celery@W1', 'time_start': 1529444404.48743, 'acknowledged': False, 'delivery_info': {'exchange': '', 'routing_key': 'tasksQB', 'priority': 1, 'redelivered': False}, 'worker_pid': 42597}
    * {'id': 'da5f5b14-6fbf-42f9-8287-73df9e7f9889', 'name': 'tasks.example_task4', 'args': '()', 'kwargs': '{}', 'type': 'tasks.example_task4', 'hostname': 'celery@W1', 'time_start': 1529444404.490226, 'acknowledged': False, 'delivery_info': {'exchange': '', 'routing_key': 'tasksQB', 'priority': 9, 'redelivered': False}, 'worker_pid': 42600}
    * {'id': '72dd8e6b-c534-47e3-b121-39d3bbb94456', 'name': 'tasks.example_task2', 'args': '()', 'kwargs': '{}', 'type': 'tasks.example_task2', 'hostname': 'celery@W1', 'time_start': 1529444404.487588, 'acknowledged': False, 'delivery_info': {'exchange': '', 'routing_key': 'tasksQA', 'priority': 9, 'redelivered': False}, 'worker_pid': 42598}

Note:
occasionally celery will throw exceptions like below and it is probably linked to [this issue](https://github.com/celery/celery/issues/3773):

>ERROR/MainProcess] Control command error: BrokenPipeError(32, 'Broken pipe')
Traceback (most recent call last):
  File "/anaconda/lib/python3.6/site-packages/celery/worker/pidbox.py", line 46, in on_message
    self.node.handle_message(body, message)
>....
