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
    # id = int(request.GET.get('id'))
    brand_name = request.GET.get('brand_name')
    px = request.GET.get('px')
    pc = request.GET.get('pc')
    pj = request.GET.get('pj')
    # 展示所有品牌
    brand_list = JdBrand.objects.filter(third_cate_id=id)
    shop_list = JdShop.objects.all()
    # 展示指定品牌商品数据

    if brand_name:
        shop_list = JdShop.objects.filter(brand_name__contains=brand_name)
    bname = brand_name
    # 排序
    if px:
        shop_list = shop_list.order_by('-total_sales')
    if pc:
        shop_list = shop_list.order_by('promote_price')
    if pj:
        shop_list = shop_list.order_by('-total_evaluates')
    bid = id
    context = {
        'brand_list': brand_list,
        'shop_list': shop_list,
        'bid':bid,
        'bname':bname,
    }

    return render(request, 'search/search.html',context)

# 分页功能
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



