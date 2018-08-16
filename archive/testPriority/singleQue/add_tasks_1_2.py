from tasks import task_1, task_2, task_3, task_4#, example_task5, example_task6, example_task7, example_task8

result1 = task_1.apply_async(queue='tasksQA', priority = 1, routing_key = 'tasksA')
result2 = task_2.apply_async(queue='tasksQA', priority = 1, routing_key = 'tasksA')