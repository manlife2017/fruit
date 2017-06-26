from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
import sys
from datetime import datetime
from django.db import transaction
sys.path.append('..')
from ttss.models import UserInfo
from ttss import user_checklogin
from cart.models import CartInfo
from order.models import OrderInfo
# Create your views here.

def order(request):
    try:
        cartid = request.GET.getlist('cart_id')
        carts = []
        orders = ''
        code = 0
        if len(cartid) > 0:
            for i in cartid:
                carts.append(CartInfo.objects.get(id=i))
        else:
            code = 1
            orderid = request.GET.get('order_id')
            orders = OrderInfo.objects.get(id=int(orderid))
        return render(request, 'place_order.html', {'display': 0, 'carts': carts, 'code': code, 'order': orders})
    except Exception as res:
        print(res)
        return redirect('/cart/')




@transaction.atomic()
@user_checklogin.login
def orderadd(request):
    get = request.GET
    carts = get.get('cart_id')
    sumprice = get.get('price')
    codenum = get.get('code_num')
    try:
        if codenum == 0:
            order_point = transaction.savepoint()
            cartlist = carts.split(',')
            userid = request.session.get('u_id')
            u = UserInfo.user.get(pk=userid)
            order = OrderInfo()
            order.ouser = u
            order.oprice = sumprice
            order.save()
            for item in cartlist:
                if item:
                    cart = CartInfo.objects.get(pk=item)
                    orderdetail = OrderDetails()
                    orderdetail.count = cart.cCount
                    orderdetail.goods = cart.cGoods
                    orderdetail.price = cart.cGoods.gprice
                    orderdetail.order = order
                    orderdetail.save()
                    cart.delete()
            return JsonResponse({'code': 1, 'url': '/user/order/'})
        else:
            # 修改订单状态
            return JsonResponse({'code': 1, 'url': '/user/order/'})
        transaction.savepoint_commit(order_point)
    except Exception as res:
        print(res)
        transaction.savepoint_rollback(order_point)
        return JsonResponse({'code': 0, 'url': '/user/order/'})


