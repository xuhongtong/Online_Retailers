from django.shortcuts import render

# Create your views here.

from main.models import JdFirstCate
# <<<<<<< Updated upstream
from search.models import JdBrand
from shop.models import JdShop
# =======
# >>>>>>> Stashed changes


def index(request):
    first_cates = JdFirstCate.objects.all()
    for first_cate in first_cates:
        second_cate_list = first_cate.jdsecondcate_set.all()
        first_cate.second_cates = second_cate_list
        for second_cate in first_cate.second_cates:
            third_cate_list = second_cate.jdthirdcate_set.all()
            second_cate.third_cates = third_cate_list
# <<<<<<< Updated upstream
    brand_list=JdBrand.objects.all()
    shop_list=JdShop.objects.all()
# =======

# >>>>>>> Stashed changes
    context = {
        'first_cates': first_cates,
        'brand_list':brand_list,
        'shop_list':shop_list,
    }
    return render(request, 'index.html', context)