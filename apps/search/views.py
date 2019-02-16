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

    # context = {
    #     'brand_list': brand_list,
    #     'shop_list': shop_list,
    #     'page_num':contacts,
    # }
    # return render(request, 'search/search.html', context)
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
    #     'contacts':contacts,
    #     'page_num': contacts,
    # }
    return render(request,'search/search.html',locals())



