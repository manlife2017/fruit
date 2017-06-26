from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import hashlib
from django.core.paginator import Paginator,Page
from .models import *
from . import user_checklogin
import sys
sys.path.append('..')
from goods.models import *
from order.models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


# 注册模块
def register(request):
    return render(request, 'df_user/register.html')


def user_add(request):
    u = request.POST
    uname = u.get('user_name')
    upwd = u.get('pwd')
    ucpwd = u.get('cpwd')
    ueamil = u.get('email')
    uallow = u.get('allow')
    if upwd == ucpwd:
        pw = hashlib.sha1(upwd.encode()).hexdigest()
        UserInfo.user.create(uname, pw, ueamil)
    return redirect('/user/login/')


# 登录模块
def login(request):
    name = request.COOKIES.get('u_name', '')
    content = {'title': '用户登录', 'error_name': 0, 'error_pw': 0, 'uname': name}
    return render(request, 'df_user/login.html', content)


# 登录验证
def check_u(request):
    info = request.POST
    name = info.get('username')
    pw = info.get('pwd')
    checked = info.get('checked', 0)
    u = UserInfo.user.all().filter(uname__exact=name)
    if len(u) == 1:
        s_pw = hashlib.sha1(pw.encode()).hexdigest()
        if s_pw == u[0].upasswd:
            url = request.COOKIES.get('url', '/')
            print(url)
            res = HttpResponseRedirect(url)
            # 用户记住密码打钩
            if checked != 0:
                res.set_cookie('u_name', u[0].uname)
            else:
                res.set_cookie('u_name', '', max_age=-1)
            request.session['u_id'] = u[0].id
            request.session['u_name'] = u[0].uname
            return res
        else:
            content = {'title': '用户登录', 'error_name': 0, 'error_pw': 1, 'uname': name, 'pw': pw}
            return render(request, 'df_user/login.html', content)
    else:
        content = {'title': '用户登录', 'error_name': 1, 'error_pw': 0, 'uname': name, 'pw': pw}
        return render(request, 'df_user/login.html', content)


# info user 用户
@user_checklogin.login
def info(request):
    good_list = []
    goods_ids = request.COOKIES.get('goods_id')
    if goods_ids:
        goodids = goods_ids.split(',')
        for i in goodids:
            good_list.append(GoodsInfo.objects.get(pk=int(i)))
    content = {'display': 0, 'goods': good_list}
    return render(request, 'df_user/user_center_info.html', content)


# 订单
@user_checklogin.login
def order(request, pagenum):
    if pagenum == '':
        pagenum = 1
    else:
        pagenum = pagenum
    uid = request.session.get('u_id')
    orders = OrderInfo.objects.filter(ouser_id=uid).order_by('-odate')
    paginator = Paginator(orders, 2)
    l_index = paginator.page_range
    page = paginator.page(pagenum)
    content = {
        'display': 0, 'page': page, 'p_list': l_index, 'index': pagenum

    }
    return render(request, 'df_user/user_center_order.html', content)


# site
@user_checklogin.login
def site(request):
    u = UserInfo.user.get(id__exact=request.session.get('u_id'))
    if request.POST:
        post = request.POST
        u.ushou = post.get('ushou')
        u.uaddress = post.get('address')
        u.uphone = post.get('uphone')
        u.uyoubian = post.get('uyoubian')
        u.save()
    content = {'info': u, 'display': 0}
    return render(request, 'df_user/user_center_site.html', content)


# quit
def quit(request):
    print(request.session.get('u_name'))
    print(request.session.get('u_id'))
    del request.session['u_name']
    del request.session['u_id']
    return redirect('/')





