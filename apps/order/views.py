from django.shortcuts import render

# Create your views here.
from shop.models import JdShop
from shopcart.models import ShopCart


def order(request):
    # 获取登陆用户购物车商品添加记录
    shop_carts = ShopCart.objects.filter(uid=request.session.get('userid'), is_valid=1)
    for shop_cart in shop_carts:
        shop_cart.title = JdShop.objects.filter(id=shop_cart.shop_id).values_list('title').first()[0]
        shop_cart.brand_name = JdShop.objects.filter(id=shop_cart.shop_id).values_list('brand_name').first()[0]
        shop_cart.promote_price = JdShop.objects.filter(id=shop_cart.shop_id).values_list('promote_price').first()[0]
        shop_cart.original_price = JdShop.objects.filter(id=shop_cart.shop_id).values_list('original_price').first()[0]
        shop_cart.img = JdShop.objects.filter(id=shop_cart.shop_id).values_list('img_url').first()[0]
    # 前端需要渲染的数据
    context = {
        'shop_carts': shop_carts,
    }
    return render(request,'order/order.html',context)