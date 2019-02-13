# -*- coding:utf-8 -*-
__author__ = 'xht'
__date__ = '2019/2/12 17:05'

from functools import wraps
from django.http import HttpResponseRedirect

def check_user_login(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        request = args[0]
        user_id = request.session.get('user_id', None)
        if user_id == None:
            return HttpResponseRedirect('/user/login')
        return func(*args, **kwargs)

    return __wrapper