from django.shortcuts import render

# Create your views here.
'''
个人中心
'''
def personal_view(request):
    '''
    个人中心
    :param request:
    :return:
    '''
    return render(request,'personal/index.html')

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

def order_manage(request):
    '''
    订单管理
    :param request:
    :return:
    '''
    return render(request,'personal/order.html')

def orderinfo_view(request):
    '''
    订单详情
    :param request:
    :return:
    '''
    return render(request,'personal/orderinfo.html')

def information_view(request):
    '''
    个人信息
    :param request:
    :return:
    '''
    return render(request,'personal/information.html')
