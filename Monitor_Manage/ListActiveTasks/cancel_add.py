from tasks import app
import time

res = app.control.cancel_consumer('tasksQA')
print('cancel tasksQA')

time.sleep(25)

res = app.control.add_consumer('tasksQA')
print('add tasksQA')

print(res)