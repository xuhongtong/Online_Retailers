import urllib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from main.models import JdThirdCate
from search.models import JdBrand
from shop.models import JdShop
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# 搜索功能
def search(request):
    request.encoding = 'utf8'
    id=request.GET.get('id')
    keyword=request.GET.get('keyword')
    # id = int(request.GET.get('id'))
    brand_name = request.GET.get('brand_name')
    sort=request.GET.get('sort')

    # 展示所有商品数据
    shop_list = JdShop.objects.all()

    # 展示指定品牌商品数据
    if keyword:
        shop_list = JdShop.objects.filter(brand_name__contains=keyword)
    # 展示所有品牌
    brand_list = JdBrand.objects.filter(third_cate_id=id)
    # 排序
    if sort:
        shop_list=shop_list.order_by(sort)

    context = {
        'brand_list': brand_list,
        'shop_list': shop_list,
    }
    return render(request, 'search/search.html', context)
# 分类功能
@login_required
def page_divide(request):
    phone_name_list=JdShop.objects.all()
    paginator=Paginator(phone_name_list,5)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    return render(request,'search/search.html',{'page_num':contacts})



