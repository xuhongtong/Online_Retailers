from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from Online_Retailers import settings
from account.hash_secret import hash_code
from account.models import User
from utils.check_user import check_user_login

'''
个人中心

'''

@check_user_login
def personal_view(request):
    '''
    个人中心入口
    验证登录
    :param request:
    :return:
    '''
    if request.session.get('is_login'):
        return render(request, 'personal/index.html')
    else:
        return render(request, 'account/login.html')



def cardlist_view(request):
    return render(request, 'personal/cardlist.html')


def bill_view(request):
    '''
    账单管理
    :param request:
    :return:
    '''
    return render(request, 'personal/bill.html')








