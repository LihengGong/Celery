from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Async task to send an e-mail notification when an order is
    successfully created
    :param order_id: ID of the order
    :return: 1 if succeed 0 else
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order in {}'.format(order.id)
    message = 'Dear {}, \n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'liheng.gong@outlook.com',
                          [order.email])
    return mail_sent
