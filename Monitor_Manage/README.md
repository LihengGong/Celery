# Monitoring and Management

There are two methods to monitor the worker status.

## Use python code
Python code provides fine-grained control for monitoring.

## Use celery tool
Shell command is more handy and its output is well-formed.
In shell command:

    celery -A tasks inspect stats
