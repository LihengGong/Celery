# Retry

A very simple program to test retry

In one shell:

`celery worker -A tasks -l info`

In another shell:

`python add_tasks_1.py&`
