# -*- coding: utf-8 -*-
from celery import shared_task
from django.core.mail import send_mail

from Online_Retailers import settings


import time

# from celery import shared_task


@shared_task
def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )
