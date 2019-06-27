from django.shortcuts import render
from django.http import HttpResponse
from qbsk.models import Qsbk1,Qbsk4,Qbsk3,Qbsk2
from django.forms import model_to_dict
import json
# Create your views here.
def home_page(request):
    page = int(request.GET.get('page'))
    pagesize = int(request.GET.get('pagesize'))
    start = (page-1)*pagesize
    end = start+pagesize
    queryset = Qsbk1.objects.all()
    result ={
        'code':1000,
        'msg':'successed'
    }
    page_list=[]
    for data in queryset[start:end]:
        page_data = model_to_dict(
            instance=data,
            fields=(
            'id','article_title','article_video'
            ,'article_tag','article_funny',
                'article_comment','article_author','article_author_profile'
            )
        )
        page_list.append(page_data)
    result['data']=page_list
    #http://127.0.0.1:8000/home_page/?page=10&pagesize=100
    return HttpResponse(json.dumps(result,ensure_ascii=False))
def details(request):
    queryset = Qbsk2.objects.all()
    result ={
        'code':1000,
        'msg':'successed'
    }
    page_list=[]
    for data in queryset:
        page_data = model_to_dict(
            instance=data,
            fields=(
            'id','details_title','details_date'
            ,'details_funny','details_content',
                'details_Published_address','details_comment',
            )
        )
        page_list.append(page_data)
    result['data']=page_list
    return HttpResponse(json.dumps(result,ensure_ascii=False))
#根据id查找
def hot_page(request):
    id= int(request.GET.get('id'))
    result = {
            'code': 1000,
            'msg': 'successed'
        }
    if id:
        try:
            queryset = Qbsk3.objects.filter(id=id).first()
            if queryset:
                data = model_to_dict(instance=queryset)
                result['data']=data
        except Exception as err:
            result['code'] = 1002
            result['msg'] = '请求异常'

    else:
        result['code'] = 10001
        result['msg'] = '缺少必要参数'
    return  HttpResponse(json.dumps(result,ensure_ascii=False))
def user_info(request):
    # page = int(request.GET.get('page'))
    # pagesize = int(request.GET.get('pagesize'))
    # start = (page-1)*pagesize
    # end = start+pagesize
    queryset = Qbsk4.objects.all()
    result ={
        'code':1000,
        'msg':'successed'
    }
    page_list=[]
    for data in queryset:
        page_data = model_to_dict(
            instance=data,
            fields=(
            'id','user_name','user_pic'
            ,'recommendations','content',
                'liveness','date_publish','likesm'
            )
        )
        page_list.append(page_data)
    result['data']=page_list
    return HttpResponse(json.dumps(result,ensure_ascii=False))