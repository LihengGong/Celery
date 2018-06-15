# Celery
Celery Configuration tests

# Priority

Conclusion: celery will honor priority as long as the tasks are submitted fast enough.

For task priority to take effect, tasks should be submitted fast enough at the same time so that worker has the chance
to sort these tasks according to their priority.


