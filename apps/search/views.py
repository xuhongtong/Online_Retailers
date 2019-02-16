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
    # 展示所有品牌
    brand_list = JdBrand.objects.filter(third_cate_id=id)
    shop_list = JdShop.objects.all()
    # 展示指定品牌商品数据

    if brand_name:
        shop_list = JdShop.objects.filter(brand_name__contains=brand_name)
    bname = brand_name
    # 排序
    px = request.GET.get('px')
    pc = request.GET.get('pc')
    pj = request.GET.get('pj')
    if px:
        shop_list = shop_list.order_by('-total_sales')
    if pc:
        shop_list = shop_list.order_by('promote_price')
    if pj:
        shop_list = shop_list.order_by('-total_evaluates')
    px1 = px
    px2 = pc
    px3 = pj
    #已有id
    bid = id
    #价格
    pt = request.GET.get('pt')
    pt2 = request.GET.get('pt2')
    pt3 = request.GET.get('pt3')
    pt4 = request.GET.get('pt4')
    if pt:
        shop_list = shop_list.filter(promote_price__lt=1000)
    if pt2:
        shop_list = shop_list.filter(promote_price__range=(1001,2000))
    if pt3:
        shop_list = shop_list.filter(promote_price__range=(2001,3000))
    if pt4:
        shop_list = shop_list.filter(promote_price__gt=3000)
    bpt = pt
    bpt2 = pt2
    bpt3 = pt3
    bpt4 = pt4
    context = {
        'brand_list': brand_list,
        'shop_list': shop_list,
        'bid':bid,
        'bname':bname,
        'bpt':bpt,
        'bpt2':bpt2,
        'bpt3':bpt3,
        'bpt4':bpt4,
        'px1':px1,
        'px2': px2,
        'px3': px3,
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



