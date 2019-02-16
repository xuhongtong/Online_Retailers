from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from shop.models import JdShop
from shopcart.context_processors import count
from shopcart.models import ShopCart
from utils.check_user import check_user_login


# 添加购物车逻辑处理
# @check_user_login
def add_cart(request):
    result = {'status': 200, 'msg': 'ok'}
    try:
        number = request.POST.get('number')
        shop_id = request.POST.get('shop_id')

        # 商品数量初始值为0
        update_number = 0
        # 商品存在就更新数量（这里初始值为1）
        if ShopCart.objects.filter(shop_id=shop_id, uid=request.session.get('userid'), is_valid=1):
            shop = ShopCart.objects.update(number=F('number') + number)
        # 如果商品不存在将商品数量设置为1，并保存
        else:
            update_number = 1
            shop = ShopCart(number=number, shop_id=shop_id, uid=request.session.get('userid'))
            shop.save()
        shop_num = ShopCart.objects.values_list('shop_id', flat=True).count()
        data = count(request)

        result.update(data)
        return JsonResponse(result)
    except Exception as e:
        result = {'status': 400, 'msg': '添加失败'}

    return render(request, 'shopcart/shopcart.html')


# 购物车页面逻辑处理
def shopcart(request):
    # 获取登陆用户购物车商品添加记录
    shop_carts = ShopCart.objects.filter(uid=request.session.get('userid'), is_delete=1)
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

    return render(request, 'shopcart/shopcart.html', context)


# 更新cart表

def update_cart(request):
    cart_id = request.GET.get('cart_id')
    number = request.GET.get('number')
    ShopCart.objects.filter(cart_id=cart_id).update(number=number)



# 删除cart表
def remove_cart(request):
    cart_id = request.GET.get('cartid')
    ShopCart.objects.filter(cart_id=cart_id).update(is_delete=0)





