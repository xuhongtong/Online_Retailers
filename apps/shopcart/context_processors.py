from shopcart.models import ShopCart

def count(request):
    shop_num = ShopCart.objects.values('shop_id').filter(user_id=request.user.id,status=1).count()
    return {'shop_num':shop_num}