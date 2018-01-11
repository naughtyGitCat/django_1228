from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Z_hosts, Z_User, Z_IP
from . import models


# Create your views here.
# def index(request):
#     return HttpResponse("index yeap!")

# def login(request):            v2
#     # return render(request,'test1228/login.html') v1
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             username = username.strip()
#         print(username,password)
#         return redirect('test1228/index/')
#     # 通过get('username', None)的调用方法，确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None；
#     # 通过if username and password: 确保用户名和密码都不为空；
#     # 通过strip()方法，将用户名前后无效的空格剪除；
#     return render(request, 'test1228/login.html')

def login(request):
    # return render(request,'test1228/login.html') v1
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都要填写"
        if username and password:
            username = username.strip()
            print(username)
            try:
                user = Z_User.objects.get(ZName=username)
                if user.ZPassword == password:
                    print(username, password)
                    message = "密码正确!"
                    print(message)
                    return redirect('/test1228/hello/')

                else:
                    message = "密码不正确!"
            except:
                message = "用户名不存在!"
        return render(request, 'test1228/login.html', {"message": message})
    return render(request,'test1228/login.html')
    # 通过get('username', None)的调用方法，确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None；
    # 通过if username and password: 确保用户名和密码都不为空；
    # 通过strip()方法，将用户名前后无效的空格剪除；


def hello(request):
    return render(request,'test1228/hello.html')

def index(request):
    latest_host_ip = Z_hosts.objects.order_by('ZID')[:5]
    output = ','.join(p.InnerIP for p in latest_host_ip)
    return HttpResponse(output)


# def index(request):
#     latest_host_name = Z_hosts.objects.order_by('ZID')[:5]
#     template = loader.get_template('test1228/index1.html')

def detail(request, question_id):
    return HttpResponse("你正在查找主机：{}".format(question_id))


def results(request, question_id):
    response = '你正在查找主机{}'
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("你正在给该主机点赞{}".format(question_id))


def logout(request):
    pass
    return redirect("test1228/index/")
