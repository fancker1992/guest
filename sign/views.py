from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == '123456':
            # return HttpResponse('login success!')
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user', username, 3600)
            return response

        else:
            return render(request, 'index.html', {'error': 'username or password error'})

    else:
        return HttpResponse('请使用post请求!')


# 发布会管理页
def event_manage(request):
    username = request.COOKIES.get('user', '')
    return render(request, 'event_manage.html', {'user': username})
