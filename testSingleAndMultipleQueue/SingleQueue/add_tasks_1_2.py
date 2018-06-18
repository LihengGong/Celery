from tasks import example_task1, example_task2, example_task3, example_task4#, example_task5, example_task6, example_task7, example_task8

result1 = example_task1.apply_async(queue='tasksQA', priority = 1, routing_key = 'tasksA')
result2 = example_task2.apply_async(queue='tasksQA', priority = 1, routing_key = 'tasksA')
#result3 = example_task3.apply_async(queue='tasksQA', priority = 9, routing_key = 'tasksA')
#result4 = example_task4.apply_async(queue='tasksQA', priority = 9, routing_key = 'tasksA')
#result5 = example_task5.apply_async(queue='tasksQ', priority = 1)
#result6 = example_task6.apply_async(queue='tasksQ', priority = 1)
#result7 = example_task7.apply_async(queue='tasksQ', priority = 1)
#result8 = example_task8.apply_async(queue='tasksQ', priority = 8)
#print(result1.get(timeout=1), result2.get(timeout=1), result3.get(timeout=1))


#celery worker -A tasks -c 4 -Q tasksQA --loglevel=info