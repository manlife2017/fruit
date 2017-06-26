from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,Page
from .models import *
# Create your views here.


def index(request):
    type_list = TypeInfo.objects.all()
    type0 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = type_list[0].goodsinfo_set.order_by('-gmoods')[0:4]
    type1 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = type_list[1].goodsinfo_set.order_by('-gmoods')[0:4]
    type2 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = type_list[2].goodsinfo_set.order_by('-gmoods')[0:4]
    type3 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = type_list[3].goodsinfo_set.order_by('-gmoods')[0:4]
    type4 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = type_list[4].goodsinfo_set.order_by('-gmoods')[0:4]
    type5 = type_list[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = type_list[5].goodsinfo_set.order_by('-gmoods')[0:4]
    content = {
        'tp0': type0, 'tp01': type01,
        'tp1': type1, 'tp11': type11,
        'tp2': type2, 'tp21': type21,
        'tp3': type3, 'tp31': type31,
        'tp4': type4, 'tp41': type41,
        'tp5': type5, 'tp51': type51,
        'display': 1,
    }
    return render(request, 'index.html', content)


def detail(request, good_id):
    good = GoodsInfo.objects.get(pk=good_id)
    moods_good = GoodsInfo.objects.all().order_by('-gmoods')[0:2]
    content = {'good': good, 'moodsg': moods_good, 'display': 1}
    res = render(request, 'detail.html', content)
    goodids = request.COOKIES.get('goods_id', '')
    if goodids != '':
        goods_ids = goodids.split(',')
        if goods_ids.count(good_id) >= 1:
            goods_ids.remove(good_id)
        goods_ids.insert(0, good_id)
        if len(goods_ids) > 5:
            goods_ids = goods_ids[0:5]
        goodids = (',').join(goods_ids)
    else:
        goodids = good_id
    res.set_cookie('goods_id', goodids)

    return res


def list(request, tp_id, p_index, order):
    t = TypeInfo.objects.get(pk=tp_id)
    t_goods = t.goodsinfo_set.order_by('-id')[0:2]
    print(t)
    if order == '1':
        goods = t.goodsinfo_set.order_by('-id')
    elif order == '2':
        goods = t.goodsinfo_set.order_by('-gprice')
    elif order == '3':
        goods = t.goodsinfo_set.order_by('-gmoods')
    paginator = Paginator(goods, 10)
    biao_list = paginator.page_range
    page = paginator.page(p_index)
    # print(page.next_page_number())
    content = {'display': 1, 'p': page, 'xiabiao': biao_list, 'p_index': p_index, 't': t,
               't_goods': t_goods, 'order': order}
    return render(request, 'list.html', content)


from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        content = super(MySearchView, self).extra_context() # 获取上下文数据
        content['num']=1
        return content
