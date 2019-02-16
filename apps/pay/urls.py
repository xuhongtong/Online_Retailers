

from django.conf.urls import url

from pay import views

urlpatterns = [
    url(r'^alipay/',views.pay_view,name='pay'),
    url(r'^order_status/',views.order_status_view,name='order_status'),
    url(r'^callback/',views.aliapy_back_url),
]
