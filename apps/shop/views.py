from django.shortcuts import render

# Create your views here.
from shop.models import JdShop


def shop(request):
    id=request.GET.get('id')
    shop=JdShop.objects.get(id=id)
    context={
        'shop':shop
    }
    return render(request,'detail/detail.html',context)
