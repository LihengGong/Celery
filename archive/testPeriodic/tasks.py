from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', backend = 'rpc://', broker = 'pyamqp://')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name = 'add every 10')

    sender.add_periodic_task(30.0, test.s('world'), expires = 10)

    sender.add_periodic_task(
        crontab(hour = 7, minute = 30, day_of_week = 1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)
