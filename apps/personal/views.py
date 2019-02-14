from django.shortcuts import render

# Create your views here.
'''
个人中心
'''

def person_center(request):
    return render(request,'personal/personal_center.html')