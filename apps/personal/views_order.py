from django.shortcuts import render

from order.models import OrderDetail, Order
from shop.models import JdShop


def order_manage(request):
    '''
    订单管理
    :param request:
    :return:
    '''
    is_delete=request.GET.get('is_delete')
    order_list=Order.objects.filter(uid=request.session.get('userid'))
    JdShop.objects.filter()
    for order in order_list:
        # orderid=order.objects.filter('oid',flat=True).filter()
        order.list=OrderDetail.objects.filter(oid=order.oid)
        for shop_img in order.list:
            shop_img.img=JdShop.objects.filter(id=shop_img.shop_id).values_list('img_url',flat=True).first()
    context={
        'order_list':order_list,
    }
    return render(request, 'personal/order.html',context)


def orderinfo_view(request):
    '''
    订单详情
    :param request:
    :return:
    '''

    return render(request, 'personal/orderinfo.html')