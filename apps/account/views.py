import hashlib
import random
import time

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

# Create your views here.


from account.models import User


# hash加密功能
def hash_code(s, salt='account'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
# 登陆账号
def login_view(request):
    if request.session.get('is_login'):  # 不允许重复登陆
        return redirect("index")
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 验证用户是否存在
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print(user.password)
            print(hash_code(password))
            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['email'] = email
                return redirect('index')
            else:
                return HttpResponse('用户名密码错误')
        else:
            return HttpResponse('用户名不存在')


# 注册账号
def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_email = User.objects.filter(email=email)
        if is_email:
            return HttpResponse('用户名已存在')
        if password1 == password2:
            # email = email
            # password1 = hash_code(password1)
            users = User(email=email, password=hash_code(password1))
            users.save()
            return redirect('login')

# 注销账号
def logout(request):
    request.session.flush()
    return redirect('login')
def reset_passwd(request):
    pass



