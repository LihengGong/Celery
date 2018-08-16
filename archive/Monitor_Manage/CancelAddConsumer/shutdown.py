from tasks import app
import time

res = app.control.broadcast('shutdown', destination = ['celery@W2'])
print('shutdown W2')

time.sleep(5)

res = app.control.broadcast('shutdown', destination = ['celery@W1'])
print('shutdown W1')

print(res)
