from shopcart.models import ShopCart


def count(request):
    shop_num = ShopCart.objects.values('shop_id').filter(uid=request.session.get('userid'),is_valid=1).count()
    return {'shop_num':shop_num}