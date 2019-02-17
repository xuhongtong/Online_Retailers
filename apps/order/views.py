import datetime
import json
import random

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# from django_ajax.decorators import ajax

from account.models import User, Address
from order.models import Order, OrderDetail
from shop.models import JdShop
from shopcart.models import ShopCart

# @ajax
def create_order(request):
    cars_str=request.GET.get('cars_str')
    num=request.GET.get('num').strip('￥')
    # 用户id
    uid = request.session.get('userid')
    # 创建订单编号
    order_code = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100000,999999)}"
    order = Order(order_code=order_code, uid=uid, total_money=num)
    # 保存订单记录
    order.save()
    # 获取id
    oid = order.oid
    if cars_str:
        cars=json.loads(cars_str)
        # 生成订单记录
        try:
            with transaction.atomic():
                sum=0
                for car in cars:
                    ShopCart.objects.all().update(is_valid=0)
                    # 修改car_id选中状态
                    ShopCart.objects.filter(cart_id=car.get('car_id')).update(is_valid=1)
                    # price=JdShop.objects.filter(id=car.get('shop_id')).values_list('promote_price').first()[0]
                    # total_money=price*num
                    # sum+=total_money
                    shop_id=ShopCart.objects.filter(cart_id=car.get('car_id')).values_list('shop_id',flat=True).first()
                    # # 商品单价
                    price=JdShop.objects.filter(id=shop_id).values_list('promote_price',flat=True).first()
                    # #选中的商品数量
                    number=ShopCart.objects.filter(cart_id=car.get('car_id'),is_valid=1).values_list('number',flat=True).first()
                    # #选中的商品名称
                    shop_name= JdShop.objects.filter(id=shop_id).values_list('title',flat=True).first()
                    order_detail=OrderDetail(oid=oid,shop_id=shop_id,shop_name=shop_name,price=price,count=number)
                    order_detail.save()

            result = {'status': 200, 'msg': 'success', 'oid': oid}
            # result.update({'sum':sum})
            return JsonResponse(result)
        except Exception as e:
            transaction.rollback()
    else:
        return None



def order(request):
    # 获取登陆用户购物车商品添加记录
    order_id=request.GET.get('order_id')
    shop_carts = ShopCart.objects.filter(uid=request.session.get('userid'), is_valid=1)
    for shop_cart in shop_carts:
        shop_cart.title = JdShop.objects.filter(id=shop_cart.shop_id).values_list('title').first()[0]
        shop_cart.brand_name = JdShop.objects.filter(id=shop_cart.shop_id, ).values_list('brand_name').first()[0]
        shop_cart.promote_price = JdShop.objects.filter(id=shop_cart.shop_id).values_list('promote_price').first()[0]
        shop_cart.original_price = JdShop.objects.filter(id=shop_cart.shop_id).values_list('original_price').first()[0]
        shop_cart.img = JdShop.objects.filter(id=shop_cart.shop_id).values_list('img_url').first()[0]
    order=Order.objects.get(oid=order_id)
    user=User.objects.get(uid=order.uid)
    address_list=Address.objects.filter(uid=order.uid).first()
    # 前端需要渲染的数据
    context = {
        'shop_carts': shop_carts,
        'order':order,
        'user':user,
        'address_list':address_list,
    }
    return render(request, 'order/order.html', context)
