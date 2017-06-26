from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import sys
sys.path.append('..')
from ttss import user_checklogin
# Create your views here.


def cart(request):
    uid = request.session.get('u_id')
    carts = CartInfo.objects.all().filter(cUId_id__exact=uid)
    if len(carts) > 0:
        content = {'display': 0, 'carts': carts}
    else:
        content = {'display': 0}
    return render(request, 'cart.html', content)


@user_checklogin.login
def add(request, g_id, count):
    uid = request.session.get('u_id')
    count = int(count)
    gid = int(g_id)
    # 判断商品是否已经存在存在就数量累加
    carts = CartInfo.objects.filter(cGoods__exact=gid, cUId__exact=uid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.cCount += count
    else:
        cart = CartInfo()
        cart.cCount = count
        cart.cGoods_id = g_id
        cart.cUId_id = uid
    cart.save()
    # 判断异步请求
    if request.is_ajax():
        return JsonResponse({'code': 0})
    else:
        return redirect('/cart/')


def edit(request, cartid, count):
    cart = CartInfo.objects.filter(pk=cartid)[0]
    if cart:
        cart.cCount = count
        cart.save()
        print(cart.cCount)
        content = {'code': 1}
    else:
        content = {'code': 0}
    return JsonResponse(content)


def delete(request, cartid):
    cart = CartInfo.objects.filter(pk=cartid)[0]
    if cart:
        cart.delete()
        content = {'code': 1}
    else:
        content = {'code': 0}
    return JsonResponse(content)
