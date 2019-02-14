import alipay
from alipay import AliPay
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Online_Retailers import settings

'''
支付模块
    支付功能
    退款功能
    退款查询
'''

def pay_view(request):
    '''
    用于创建用于支付的对象
    :param request:
    :return:
    '''
    alipay = AliPay(
        appid=settings.APP_ID,
        app_notify_url=None,  # 默认回调url
        app_private_key_string=settings.APP_PRIVATE_STRING,
        alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True  # 默认False  配合沙箱模式使用
    )
    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
    	# 订单号
        out_trade_no='654321',
        # 商品总价
        total_amount=str(0.01),  # 将Decimal类型转换为字符串交给支付宝
        # 订单标题
        subject="天猫商城-{}".format(123456),
        # 支付成功之后 前端跳转的界面
        return_url='https://127.0.0.1:8000/',
        # 支付成功后台跳转接口
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    # 让用户进行支付的支付宝页面网址
    url = settings.ALI_PAY_URL + "?" + order_string
    return redirect(url)

@csrf_exempt
def aliapy_back_url(request):
    '''
    支付成功回调
    :param request:
    :return:
    '''
    return redirect('index')

def cancel_order(out_trade_no:int, cancel_time=None):
    '''
    撤销订单
    :param out_trade_no:
    :param cancel_time: 撤销前的等待时间(若未支付)，撤销后在商家中心-交易下的交易状态显示为"关闭"
    :return:
    '''
    result = alipay.api_alipay_trade_cancel(out_trade_no=out_trade_no)
    resp_state = result.get('msg')
    action = result.get('action')
    if resp_state=='Success':
        if action=='close':
            if cancel_time:
                print("%s秒内未支付订单，订单已被取消！" % cancel_time)
        elif action=='refund':
            print('该笔交易目前状态为：',action)
        return action
    else:
        print('请求失败：',resp_state)


def need_refund(out_trade_no: str or int, refund_amount: int or float, out_request_no: str):
    '''
    退款操作
    :param out_trade_no: 商户订单号
    :param refund_amount: 退款金额，小于等于订单金额
    :param out_request_no: 商户自定义参数，用来标识该次退款请求的唯一性,可使用 out_trade_no_退款金额*100 的构造方式
    :return:
    '''
    result = init_alipay_cfg().api_alipay_trade_refund(out_trade_no=out_trade_no,
                                                       refund_amount=refund_amount,
                                                       out_request_no=out_request_no)

    if result["code"] == "10000":
        return result  # 接口调用成功则返回result
    else:
        return result["msg"]  # 接口调用失败则返回原因

def refund_query(out_request_no:str, out_trade_no:str or int):
    '''
    退款查询：同一笔交易可能有多次退款操作（每次退一部分）
    :param out_request_no: 商户自定义的单次退款请求标识符
    :param out_trade_no: 商户订单号
    :return:
    '''
    result = alipay.api_alipay_trade_fastpay_refund_query(out_request_no, out_trade_no=out_trade_no)
    if result["code"] == "10000":
        return result  #接口调用成功则返回result
    else:
        pass