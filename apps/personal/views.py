from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from account.models import User

'''
个人中心
'''

def personal_view(request):
    '''
    个人中心入口
    :param request:
    :return:
    '''
    if request.session['is_login']:
        return render(request,'personal/index.html')
    else:
        return render(request,'account/login.html')

# 个人信息
def information_view(request):
    '''
    个人信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        content = {'nickname':user.nickname,
                   'name':user.name,
                   'email':user.email,
                   'sex':user.sex,
                   'phone': user.phone,
                   'birthday':user.birthday,
                   }
        return render(request, 'personal/information.html', content)
    elif request.method == 'POST':
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        nickname = request.POST.get('nickname')
        if not nickname:
            nickname = user.nickname
        name = request.POST.get('name')
        if not name:
            name=user.name
        sex = request.POST.get('sex')
        if not sex:
            sex = user.sex
        phone = request.POST.get('phone')
        if not phone:
            phone = user.phone
        email = request.POST.get('email')
        if not email:
            email = user.email
        try:
            User.objects.filter(uid=uid).update(nickname=nickname,name=name,sex=sex,phone=phone,email=email)
            return redirect('information')
        except Exception as e:
            print(e)



# 安全设置
def safety_view(request):
    if request.method=="GET":
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        content = {'nickname':user.nickname,
                   'name':user.name,
                   'email':user.email,
                   'sex':user.sex,
                   'phone': user.phone,
                   'birthday':user.birthday,
                   }
        return render(request, 'personal/information.html', content)
    elif request.method == 'POST':
        return redirect('safery')





def bill_view(request):
    '''
    账单管理
    :param request:
    :return:
    '''
    return render(request,'personal/bill.html')


def address_view(request):
    '''
    地址管理
    :param request:
    :return:
    '''
    return render(request,'personal/address.html')

def order_manage(request):
    '''
    订单管理
    :param request:
    :return:
    '''
    return render(request,'personal/order.html')

def orderinfo_view(request):
    '''
    订单详情
    :param request:
    :return:
    '''
    return render(request,'personal/orderinfo.html')


