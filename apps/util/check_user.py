# -*- coding:utf-8 -*-
from django.shortcuts import redirect
from django.urls import reverse

__author__ = 'xht'
__date__ = '2019/2/12 17:05'

from functools import wraps
from django.http import HttpResponseRedirect

def check_user_login(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        request = args[0]
        path=request.path
        user_id = request.session.get('userid', None)
        if user_id == None:
            uri = reverse("login")
            return redirect(f'{uri}?next={path}')
        return func(*args, **kwargs)

    return __wrapper