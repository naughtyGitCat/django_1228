from django.shortcuts import render
from django.shortcuts import redirect
# def hello(request):
#     context = {}
#     context['hello'] =  'hello django'
#     return render(request,'hello.html',context)


def hello(request):
    return render(request, 'hello.html')
    # return redirect('/hello.html')
