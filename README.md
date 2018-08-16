# Celery + rabbitMQ + Django

Integrating Celery into Django is quite simple. And with simple settings, rabbitMQ can be used as the broker for Celery.

With this setup, asynchronous tasks can be "delegated" to Celery.

Django_Celery_send_mail is a sample project to showcase how to send mail asynchronously with Celery.