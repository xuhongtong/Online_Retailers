# 个人信息
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from account.models import User


def information_view(request):
    '''
    个人信息
    :param request:
    :return:
    '''
    if request.method == 'GET':
        uid = request.session.get('userid')
        user = User.objects.filter(uid=uid).first()
        birthday = User.objects.filter(uid=uid).values_list('birthday').first()[0]
        str_birthday = datetime.datetime.strftime(birthday, '%Y-%m-%d')
        year = str_birthday.split('-')[0]
        month = str_birthday.split('-')[1]
        day = str_birthday.split('-')[2]
        content = {'nickname': user.nickname,
                   'name': user.name,
                   'email': user.email,
                   'sex': user.sex,
                   'phone': user.phone,
                   'birthday': user.birthday,
                   'year': year,
                   'month': month,
                   'day': day,
                   }
        return render(request, 'personal/information.html', content)
    elif request.method == 'POST':
        # 修改用户信息: 用户名,昵称名,性别,电话,邮箱,
        uid = request.session.get('userid')
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
        if year and month and day:
            birthday = year + '-' + month + '-' + day
        else:
            birthday = user.birthday
        User.objects.filter(uid=uid).update(nickname=nickname, name=name, sex=sex, phone=phone, email=email,
                                            birthday=birthday)
        return redirect('information')

