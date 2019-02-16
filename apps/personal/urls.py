
from django.contrib import admin
from django.conf.urls import url, include
from personal import views, views_info, views_safety, views_address, views_order

urlpatterns = [
    # 个人中心主页
    url(r'^personal/', views.personal_view, name='personal'),
    # 个人中心个人信息页
    url(r'^information/',views_info.information_view,name='information'),


    # 安全设置
    url(r'^safety/',views_safety.safety_view,name='safety'),
    # 修改密码
    url(r'password_update/',views_safety.password_update_view,name='password_update'),
    # 设置支付密码
    url(r'^setpay/',views_safety.setpay_view,name='setpay'),

    # 地址管理
    url(r'^address/',views_address.address_view,name='address'),
    # 快捷支付
    url(r'^cardlist/',views.cardlist_view,name='cardlist'),
    # 邮箱验证
    url(r'^email/',views_safety.email_view,name='email'),
    url(r'^bill/',views.bill_view,name='bill'),
    url(r'^order_manage/',views_order.order_manage,name='order_manage'),
    url(r'^orderinfo/',views_order.orderinfo_view,name='orderinfo'),


]

