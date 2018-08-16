from tasks import example_task1, example_task2, example_task3, example_task4#, example_task5, example_task6, example_task7, example_task8


result3 = example_task3.apply_async(queue='tasksQLong', priority = 1, routing_key = 'tasksLong')
result4 = example_task4.apply_async(queue='tasksQLong', priority = 1, routing_key = 'tasksLong')
