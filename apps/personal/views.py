
from django.shortcuts import render


'''
个人中心
'''


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








