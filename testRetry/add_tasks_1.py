from tasks import task_1

result1 = task_1.apply_async(queue = 'tasksQA', priority = 1, routing_key = 'tasksA')
