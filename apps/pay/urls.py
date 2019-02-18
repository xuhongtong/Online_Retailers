

from django.conf.urls import url

from pay import views

urlpatterns = [
    url(r'^alipay/',views.pay_view,name='pay'),
    url(r'^success/',views.success_view,name='success'),
    url(r'^callback/',views.aliapy_back_url),
]
