# 安全设置
import ajax as ajax
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader

from Online_Retailers import settings
from account.hash_secret import hash_code
from account.models import User
from personal.models import QuestionSafety


def safety_view(request):
    '''
    安全设置
    账户安全分数计算
    :param request:
    :return:
    '''
    if request.method == "GET":
        uid = request.session.get('userid')
        user = User.objects.filter(uid=uid).first()
        content = {
            'safety_score': user.safety_score,
            'email': user.email,
            'nickname': user.nickname,
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
            uid = request.session.get('userid')
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
    if request.method == 'GET':
        return render(request, 'personal/setpay.html')


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
    if request.method == 'GET':
        uid = request.session.get('userid')
        user = User.objects.filter(uid=uid).first()
        content = {'email': user.email}
        return render(request, 'personal/email.html', content)
    if request.method == 'POST':
        email = request.POST.get('email')
        content = loader.render_to_string('account/mail.html', request=request)
        send_mail(subject='xxx线上xxx绑定邮件',
                  message='',
                  html_message=content,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email]
                  )
        return render(request, 'msg.html')


def question_view(request):
    if request.method =='GET':
        uid = request.session.get('uid')
        questions = User.objects.filter(uid=uid).values('questionsafety__question')
    return render(request, 'personal/question.html')
