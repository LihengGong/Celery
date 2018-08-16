from tasks import example_task1, example_task2, example_task3, example_task4#, example_task5, example_task6, example_task7, example_task8

result1 = example_task1.apply_async(queue='tasksQA', priority = 1, routing_key = 'tasksA')
result2 = example_task2.apply_async(queue='tasksQA', priority = 9, routing_key = 'tasksA')
