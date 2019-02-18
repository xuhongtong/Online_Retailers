from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from search.models import JdBrand
from shop.models import JdShop
from django.db.models import Q
def search(request):
    request.encoding='utf8'
    # id=request.GET.get('third_cate_id')
    kw=request.GET.get('keyword')
    shop_list=JdShop.objects.all()
    if kw:
        shop_list = JdShop.objects.filter(Q(brand_name__contains=kw)|Q(title__contains=kw))
        id=shop_list.values_list('third_cate_id',flat=True).first()
        brand_list=JdBrand.objects.filter(third_cate_id=id)
    # third_cate_id=shop_list.values_list('third_cate_id').first()
    # brand_list = JdBrand.objects.filter(third_cate_id=id)
    # 分页功能
    paginator = Paginator(shop_list, 8)  # 每页展示的数据
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
    return render(request, 'search_key/search_key.html', locals())

