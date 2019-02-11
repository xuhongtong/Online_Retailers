import urllib

from django.shortcuts import render

# Create your views here.
from main.models import JdThirdCate
from search.models import JdBrand
from shop.models import JdShop


def search(request):

    request.encoding = 'utf8'
    id=request.GET.get('id')
    id = int(request.GET.get('id'))
    brand_name = request.GET.get('brand_name')

    # 展示所有商品数据
    shop_list = JdShop.objects.all()

    # 展示指定品牌商品数据
    if brand_name:
        shop_list = JdShop.objects.filter(brand_name=brand_name)

    # 展示所有品牌
    brand_list = JdBrand.objects.filter(third_cate_id=id)

    # 排序

    shop_list=shop_list.order_by('total_sales')

    context = {
        'brand_list': brand_list,
        'shop_list': shop_list,
    }
    return render(request, 'search/search.html', context)


