
from datetime import datetime

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from itsdangerous import URLSafeSerializer

from Online_Retailers import settings
from account.hash_secret import hash_code
from account.models import User


'''
功能点
登录
注册
异步邮件
验证码
改密
'''

# hash加密功能
from account.task import send_active_mail

def login_view(request):
    '''
    登录,
    验证码
    :param request:
    :return:
    '''
    if request.session.get('is_login'):  # 不允许重复登陆
        return redirect("index")
    if request.method == 'GET':
        # 获取header中的数据
        next1=request.META.get('HTTP_REFERER','/')

        # 生成验证码,由验证码模块完成
        key = CaptchaStore.generate_key()
        img_url = captcha_image_url(key)

        return render(request, 'account/login.html', context={'next1': next1, 'img_url': img_url, 'key': key})

    if request.method == 'POST':
        # 获取输入的验证码
        code = request.POST.get('code')
        # 验证码的key,从后端传到前端再传回后端的值
        key = request.POST.get('key')
        # 获取用户名密码
        usr = request.POST.get('nickname')
        password = request.POST.get('password')
        # 生成验证码图片链接
        img_url = captcha_image_url(key)
        # 获取重定向坐标
        next1 = request.POST.get('next1', '/')

        if usr and password and code :
            # 验证用户是否存在
            if User.objects.filter(Q(nickname=usr) | Q(email=usr)).exists():
                # 通过昵称或者email来从数据库获取用户信息
                user = User.objects.filter(Q(nickname=usr) | Q(email=usr)).first()
                # 验证输入的密码和用户密码是否一致
                if hash_code(password)  == user.password:
                    # 验证用户账户是否已经激活
                    if user.active:
                        # 获取验证码对象
                        cap_obj = CaptchaStore.objects.filter(hashkey=key).first()
                        # 获取失效时间，与当前时间进行比较
                        expiration = cap_obj.expiration
                        # 获取response值
                        response = cap_obj.response
                        if datetime.now() < expiration and code.lower() == response:
                            # 验证码验证成功

                            # 登陆成功，记住登录状态
                            request.session['userid']=user.uid
                            request.session['is_login'] = True
                            request.session['email'] = user.nickname

                            return redirect(next1)
                        else:
                            # 验证失败，重新刷新验证码
                            key = CaptchaStore.generate_key()
                            img_url = captcha_image_url(key)
                            return render(request,'account/login.html',{'capt_error':'验证码错误,点击刷新','key':key,'img_url':img_url})

                    else:
                        return render(request, 'account/login.html',
                                      {'login_msg': '用户未激活', 'img_url': img_url, 'key': key, 'next1': next1})
                else:
                    return render(request, 'account/login.html',
                                  {'login_msg': '账号或密码错误', 'img_url': img_url, 'key': key, 'next1': next1})
            else:
                return render(request, 'account/login.html',
                              {'login_msg': '用户不存在', 'img_url': img_url, 'key': key, 'next1': next1})
        else:
            return render(request, 'account/login.html',
                          {'capt_error': '账号或密码或验证码不能为空', 'img_url': img_url, 'key': key, 'next1': next1})

def register(request):
    '''
    注册账号
    异步发送邮件
    :param request:
    :return:
    '''
    if request.method == 'GET':
        # 返回注册界面
        return render(request, 'account/register.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_user = User.objects.filter(nickname=username)
        if is_user:
            return HttpResponse('用户名已存在')
        if password1 == password2:

            # password1 = hash_code(password1)
            # 保存用户到数据库

            user = User(email=email, nickname=username, password=hash_code(password1))
            user.save()
            try:
                auth_s = URLSafeSerializer(settings.SECRET_KEY, 'auth')
                token = auth_s.dumps({'name': username})
                cache.set(token, user.uid, timeout=10 * 60)
                active_url = f'http://127.0.0.1:8000/account/active/?tooken={token}'
                content = loader.render_to_string('account/mail.html', request=request,
                                                  context={'username': username, 'active_url': active_url})
                send_active_mail.delay(subject='手机交易平台激活邮件', content=content, to=[email])
                return render(request, 'account/active_email.html')
            except Exception as e:
                    print(e)
        else:
            pass
        return redirect('/')


# xxx/active/?token=afsfsdfs
def active_account(request):
    '''
    账号激活
    :param request:
    :return:
    '''
    token = request.GET.get('tooken')
    uid = cache.get(token)
    if uid:
        User.objects.filter(uid=uid).update(active=1)
        return redirect('login')
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询user对象
        return redirect('/')



def logout_view(request):
    '''
    退出登录
    :param request:
    :return:
    '''
    request.session.flush()
    return redirect('/')

# @login_required(login_url='login')
# def logout_view(request):
#     # 表示登出
#     next1 = request.META.get('HTTP_REFERER', '/')
#     logout(request)
#     return redirect(next1)


# def send_active_mail(subject='', content=None, to=None):
#     send_mail(subject=subject,
#               message='',
#               html_message=content,
#               from_email=settings.EMAIL_HOST_USER,
#               recipient_list=to
#               )


def refresh_code(request):
    '''
    刷新验证码
    :param request:
    :return:
    '''
    key = CaptchaStore.generate_key()
    img_url = captcha_image_url(key)
    return JsonResponse({'key': key, 'img_url': img_url})

# 异步,验证码,三方登录,手机验证码