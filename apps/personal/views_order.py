from django.shortcuts import render


def order_manage(request):
    '''
    订单管理
    :param request:
    :return:
    '''
    return render(request, 'personal/order.html')


def orderinfo_view(request):
    '''
    订单详情
    :param request:
    :return:
    '''
    return render(request, 'personal/orderinfo.html')