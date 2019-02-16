from django.shortcuts import render


def address_view(request):
    '''
    地址管理
    :param request:
    :return:
    '''
    return render(request, 'personal/address.html')