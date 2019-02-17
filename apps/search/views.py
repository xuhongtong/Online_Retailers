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
    brand_name_keyword=request.GET.get('keyword')
    # id = int(request.GET.get('id'))
    # brand_name = request.GET.get('brand_name')
    # sort=request.GET.get('sort')
    # 展示所有商品数据
    shop_list = JdShop.objects.all()
    # 展示指定品牌商品数据
    if brand_name_keyword:
        shop_list = JdShop.objects.filter(brand_name__contains=brand_name_keyword)
    # 展示所有品牌
    brand_list = JdBrand.objects.filter(third_cate_id=id)
    bname=brand_name_keyword
    # # 排序
    # if sort:
    #     shop_list=shop_list.order_by(sort)
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
# 分页功能
    paginator = Paginator(shop_list, 8)#每页展示的数据
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    if page > paginator.num_pages:
        page = 1
    contacts = paginator.page(page)
    num_pages = paginator.num_pages
    if num_pages < 5:
        # 1-num_pages
        pages = range(1, num_pages + 1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        # num_pages-4, num_pages
        pages = range(num_pages - 4, num_pages + 1)
    else:
        # page-2, page+2
        pages = range(page - 2, page + 3)
    # context = {
    #     'brand_list': brand_list,
    #     'shop_list': shop_list,
    #     'bid': bid,
    #     'bname': bname,
    #     'bpt': bpt,
    #     'bpt2': bpt2,
    #     'bpt3': bpt3,
    #     'bpt4': bpt4,
    #     'px1': px1,
    #     'px2': px2,
    #     'px3': px3,
    #     'contacts':contacts,
    #     'pages':pages,
    # }
    return render(request,'search/search.html',locals())


