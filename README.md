# Celery
Celery Configuration tests

Various configurations are tested.

## Priority

Conclusion: celery will honor priority as long as the tasks are submitted fast enough(i.e. at almost the same time).

| Tables        | Single Queue  | Double Queue  |
| ------------- |:-------------:|:-----:|
| Priority      | Yes           | Yes in both queues |


## Retry

Still working on the test code. Will update.