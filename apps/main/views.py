from django.shortcuts import render

# Create your views here.

from main.models import JdFirstCate

from search.models import JdBrand
from shop.models import JdShop



def index(request):
    first_cates = JdFirstCate.objects.all()
    for first_cate in first_cates:
        second_cate_list = first_cate.jdsecondcate_set.all()
        first_cate.second_cates = second_cate_list
        for second_cate in first_cate.second_cates:
            third_cate_list = second_cate.jdthirdcate_set.all()
            second_cate.third_cates = third_cate_list
    # 获取商品数据
    shop_list = JdShop.objects.all()
    brand_list = JdBrand.objects.all()
    shops = shop_list.filter(id__lt=7)
    brands = brand_list.filter(brand_id__lt=4)
    shop1 = shop_list.filter(brand_name='Apple', id__lt=6)
    context = {
        'first_cates': first_cates,
        'brand_list':brand_list,
        'shop_list':shop_list,
        'brands': brands,
        'shops': shops,
        'shop1':shop1,
    }
    return render(request, 'index.html', context)