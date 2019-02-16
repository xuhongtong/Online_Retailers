# 个人信息
from django.shortcuts import redirect, render

from account.models import User


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
        uid = request.session.get('userid')
        user = User.objects.filter(uid=uid).first()
        if user.birthday:
            year = user.birthday.split('-')[0]
            month = user.birthday.split('-')[1]
            day = user.birthday.split('-')[2]
        content = {'nickname': user.nickname,
                   'name': user.name,
                   'email': user.email,
                   'sex': user.sex,
                   'phone': user.phone,
                   # 'year':year,'month':month,'day':day,
                   'year_list':year_list,'month_list':month_list,'day_list':day_list,
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
        birthday = year + '-' + month + '-' + day
        try:
            if birthday !='1970-1-1':
                User.objects.filter(uid=uid).update(nickname=nickname, name=name, sex=sex, phone=phone, email=email,birthday=birthday)
                return redirect('information')

        except Exception as e:
            print(e)