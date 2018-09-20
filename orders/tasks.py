from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def OrderCreated(order_id):
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear, {}, order successfuly placed.\
               your order number {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_send