from django.shortcuts import render , HttpResponse, redirect
from django.core.paginator import Paginator
from myapp.models import Newswrite,Sports, Technology,Breaking

# Create your views here.
def index(request):
    return render(request,'index.html')
def politics(request):
    news_list = Newswrite.objects.all().order_by('-date')
    paginator = Paginator(news_list,2)#putting limit in data
    page_num = request.GET.get('page')#Getting page no
    service_detail = paginator.get_page(page_num)#Final data

    data = {
        'service_detail':service_detail,
        'news_list':news_list,
    }
    
    return render(request,'politics.html',data)
def breaking(request):
    breaking = Breaking.objects.all().order_by('-date')
    data = {
        'news_list':breaking
    }
    
    return render(request,'breaking.html',data)

def breaking_detail(request,pk):
    news_list = Breaking.objects.get(id=pk)
    news_list2 = Breaking.objects.all().order_by('-date')
    data = {
        'news_list':news_list,
        'news_list2':news_list2,
    }
    return render( request,'breaking_details.html',data)

    
def politics_detail(request,pk):
    news_list = Newswrite.objects.get(id=pk)
    news_list2 = Newswrite.objects.all().order_by('-date')
    data = {
        'news_list':news_list,
        'news_list2':news_list2,
    }
    return render( request,'politics_details.html',data)


def technology(request):
    news_list = Technology.objects.all().order_by('-date')
    data = {
        'news_list':news_list
    }
    return render(request,'technology.html',data)
def technology_detail(request,pk):
    news_list = Technology.objects.get(id=pk)
    news_list2 = Technology.objects.all().order_by('-date')
    data = {
        'news_list':news_list,
        'news_list2':news_list2,

    }
    return  render(request,'technology_details.html', data)
def sports(request):
    news_list = Sports.objects.all().order_by('-date')
    data = {
        'news_list':news_list
    }
    return render(request,'sports.html',data)

def sports_detail(request,pk):
    news_list = Sports.objects.get(id=pk)
    news_list2 = Sports.objects.all().order_by('-date')
    data ={
        'news_list':news_list,
        'news_list2':news_list2,
    }
    return render(request,'sports_details.html',data)


