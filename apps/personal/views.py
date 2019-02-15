from django.shortcuts import render

# Create your views here.
'''
个人中心
'''

def bill_view(request):
    '''
    账单管理
    :param request:
    :return:
    '''
    return render(request,'personal/bill.html')


def address_view(request):
    '''
    地址管理
    :param request:
    :return:
    '''
    return render(request,'personal/address.html')

