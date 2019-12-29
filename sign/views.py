from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == '123456':
            return HttpResponse('login success!')
        else:
            return render(request, 'index.html', {'error': 'username or password error'})
    else:
        return HttpResponse('请使用post请求!')
