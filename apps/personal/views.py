from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from Online_Retailers import settings
from account.hash_secret import hash_code
from account.models import User

'''
个人中心

'''


def personal_view(request):
    '''
    个人中心入口
    验证登录
    :param request:
    :return:
    '''
    if request.session['is_login']:
        return render(request, 'personal/index.html')
    else:
        return render(request, 'account/login.html')


# 个人信息
def information_view(request):
    '''
    个人信息
    :param request:
    :return:
    '''
    if request.method == 'GET':
        year_list = [i for i in range(1970,2020)]
        month_list = [i for i in range(1,13)]
        day_list = [i for i in range(1,32)]
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        year = user.birthday.split('-')[0]
        month = user.birthday.split('-')[1]
        day = user.birthday.split('-')[2]
        content = {'nickname': user.nickname,
                   'name': user.name,
                   'email': user.email,
                   'sex': user.sex,
                   'phone': user.phone,
                   'year':year,'month':month,'day':day,
                   'year_list':year_list,'month_list':month_list,'day_list':day_list,
                   }
        return render(request, 'personal/information.html', content)
    elif request.method == 'POST':
        # 修改用户信息: 用户名,昵称名,性别,电话,邮箱,
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        nickname = request.POST.get('nickname')
        if not nickname:
            nickname = user.nickname
        name = request.POST.get('name')
        if not name:
            name = user.name
        sex = request.POST.get('sex')
        if not sex:
            sex = user.sex
        phone = request.POST.get('phone')
        if not phone:
            phone = user.phone
        email = request.POST.get('email')
        if not email:
            email = user.email
        # 获取生日年月日信息
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')
        birthday = year + '-' + month + '-' + day
        try:
            if birthday !='1970-1-1':
                User.objects.filter(uid=uid).update(nickname=nickname, name=name, sex=sex, phone=phone, email=email,birthday=birthday)
                return redirect('information')

        except Exception as e:
            print(e)

# 安全设置
def safety_view(request):
    '''
    安全设置
    账户安全分数计算
    :param request:
    :return:
    '''
    if request.method == "GET":
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        content = {'nickname': user.nickname,
                   'safety_score': user.safety_score,
                   'email':user.email,
                   }
        return render(request, 'personal/safety.html', content)
    elif request.method == 'POST':
        return redirect('safery')


# 修改密码
def password_update_view(request):
    '''
    更改密码
    :param request:
    :return:
    '''
    try:
        if request.method == 'GET':
            return render(request, 'personal/password.html')
        if request.method == 'POST':
            # 获取页面用户名,锁定数据库用户信息
            uid = request.session['userid']
            user = User.objects.filter(uid=uid).first()
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            verify_password = request.POST.get('verify_password')
            # 验证原密码是否正确
            if user.password == hash_code(old_password):
                # 验证两次输入密码是否一致
                if verify_password == new_password:
                    # 验证新旧密码不相同,保存新密码
                    if new_password != old_password:
                        user.password = hash_code(new_password)
                        user.save()
                        request.session.flush()
                        return redirect('login')
                    else:
                        return render(request, 'personal/password.html', {'msg': '新密码不能与旧密码相同，请重新输入'})
                else:
                    return render(request, 'personal/password.html', {'msg': '两次密码不一致,请重新输入'})
            else:
                return render(request, 'personal/password.html', {'msg': '您的密码输入错误,请重新输入'})
    except Exception as e:
        return render(request, 'account/404.html', {'msg': e})

# 设置支付密码
def setpay_view(request):
    if request.method=='GET':
        return render(request,'personal/setpay.html')


# 邮箱验证
def email_view(request):
    """
        subject,标题
        message, 邮件的内容
        from_email,发送邮件者
        recipient_list,  接受邮件列表
        html_message = 邮件的内容,以html格式显示邮件内容
    :param request:
    :return:
    """
    if request.method=='GET':
        uid = request.session['userid']
        user = User.objects.filter(uid=uid).first()
        content = {'email':user.email}
        return render(request,'personal/email.html',content)
    if request.method=='POST':
        email = request.POST.get('email')
        content = loader.render_to_string('account/mail.html', request=request)
        send_mail(subject='xxx线上xxx绑定邮件',
                  message='',
                  html_message=content,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email]
                  )
        return render(request, 'msg.html')

def cardlist_view(request):
    return render(request, 'personal/cardlist.html')


def bill_view(request):
    '''
    账单管理
    :param request:
    :return:
    '''
    return render(request, 'personal/bill.html')


def address_view(request):
    '''
    地址管理
    :param request:
    :return:
    '''
    return render(request, 'personal/address.html')


def order_manage(request):
    '''
    订单管理
    :param request:
    :return:
    '''
    return render(request, 'personal/order.html')


def orderinfo_view(request):
    '''
    订单详情
    :param request:
    :return:
    '''
    return render(request, 'personal/orderinfo.html')
