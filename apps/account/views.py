import hashlib

# from captcha.helpers import captcha_image_url
# from captcha.models import CaptchaStore
from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from itsdangerous import URLSafeSerializer

from Online_Retailers import settings
from account.models import User


# from account.task import send_active_mail

# hash加密功能
from account.task import send_active_mail


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
        return render(request,'account/login.html')
        # next1 = request.META.get('HTTP_REFERER', '/')
        # # 生成验证码
        # key = CaptchaStore.generate_key()
        # img_url = captcha_image_url(key)
        # return render(request, 'account/login.html', context={'next1': next1, 'img_url': img_url, 'key': key})
    if request.method == 'POST':
        usr = request.POST.get('user-name')
        password = request.POST.get('password')
        # 验证用户是否存在
        if User.objects.filter(Q(username=usr) | Q(email=usr)).exists():
            user = User.objects.filter(Q(username=usr) | Q(email=usr)).first()
            # print(user.password)
            # print(hash_code(password))
            if user.active == 1:
                if user.password == hash_code(password):
                    request.session['userid']=user.uid
                    request.session['is_login'] = True
                    request.session['email'] = user.username
                    return redirect('index')
                else:
                    return HttpResponse('用户名密码错误')
            else:
                return HttpResponse('该用户未激活')
        else:
            return HttpResponse('用户名不存在')


# 修改密码
def update_view(request):
    try:
        if request.method == 'GET':
            return render(request, 'account/update.html')
        if request.method == 'POST':
            # 获取页面用户名,锁定数据库用户信息
            username = request.POST.get('username')
            user = User.objects.filter(username=username).first()
            if user:
                oldpassword = user.password
                password = request.POST.get('password')
                # 验证旧密码
                hash = hash_code(password)
                if oldpassword == hash_code(password):
                    newpassword = request.POST.get('newpassword')
                    new_passwd = hash_code(newpassword)
                    # 验证新旧密码不相同,保存新密码
                    if new_passwd != oldpassword:
                        user = User.objects.filter(username=username).first()
                        user.password = new_passwd
                        user.save()
                        return redirect('/account/login')
                    else:
                        return render(request, 'account/update.html', {'msg': '新密码不能与旧密码相同，修改失败'})
                else:
                    return render(request, 'account/update.html', {'msg': '原密码错误，修改失败'})
            else:
                return render(request, 'account/update.html', {'msg': '账户不存在，修改失败'})
    except Exception as e:
        return render(request, 'account/404.html', {'msg': e})


# 注册账号
def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        # phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_user = User.objects.filter(username=username)
        if is_user:
            return HttpResponse('用户名已存在')
        if password1 == password2:

            # password1 = hash_code(password1)
            # 保存用户到数据库

            user = User(email=email, username=username, password=hash_code(password1))
            user.save()
            try:
                auth_s = URLSafeSerializer(settings.SECRET_KEY, 'auth')
                token = auth_s.dumps({'name': username})
                cache.set(token, user.uid, timeout=10 * 60)
                active_url = f'http://127.0.0.1:8000/account/active/?tooken={token}'
                content = loader.render_to_string('account/mail.html', request=request,
                                                  context={'username': username, 'active_url': active_url})
                send_active_mail(subject='手机交易平台激活邮件', content=content, to=[email])
                return render(request, 'account/active_email.html')
            except Exception as e:
                print(e)
        else:
            pass
        return redirect('/')


# xxx/active/?token=afsfsdfs
def active_account(request):
    token = request.GET.get('tooken')
    uid = cache.get(token)
    if uid:
        User.objects.filter(uid=uid).update(active=1)
        return redirect('login')
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询user对象
        return redirect('/')


# 注销账号
def logout_view(request):
    request.session.flush()
    return redirect('login')


# def send_active_mail(subject='', content=None, to=None):
#     send_mail(subject=subject,
#               message='',
#               html_message=content,
#               from_email=settings.EMAIL_HOST_USER,
#               recipient_list=to
#               )


# 异步,验证码,三方登录,手机验证码