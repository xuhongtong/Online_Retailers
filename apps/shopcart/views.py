from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from shopcart.context_processors import count
from shopcart.models import ShopCart

def shopcart(request):
    result = {'status': 200, 'msg': 'ok'}
    try:
        number = request.POST.get('number')
        shop_id = request.POST.get('shop_id')

        # 商品数量初始值为0
        update_number = 0
        # 商品存在就更新数量（这里初始值为1）
        if ShopCart.objects.filter(shop_id=shop_id, uid=request.user.id, status=1):
            shop = ShopCart.objects.update(number=F('number') + number)
        # 如果商品不存在将商品数量设置为1，并保存
        else:
            update_number = 1
            shop = ShopCart(number=number, shop_id=shop_id, user_id=request.user.id)
            shop.save()
        shop_num = ShopCart.objects.values_list('shop_id', flat=True).count()
        data = count(request)
        result.update(data)
        return JsonResponse(result)
    except Exception as e:
        result = {'status': 400, 'msg': '添加失败'}
    return render(request,'shopcart/shopcart.html')