from tasks import task_1, task_2, task_3, task_4#, example_task5, example_task6, example_task7, example_task8

result3 = task_3.apply_async(queue='tasksQA', priority = 9, routing_key = 'tasksA')
result4 = task_4.apply_async(queue='tasksQA', priority = 9, routing_key = 'tasksA')