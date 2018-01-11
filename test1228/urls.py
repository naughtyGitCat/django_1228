from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns=[
    #ex:/test1228/
    # url(r'^$',views.index,name='index'),
    url('index/',views.index ),
    # ex:/test1228/5/
    # ex: /polls/5/
    url('login/',views.login ),
    path('hello/',views.hello),
    # 命名分组就是给具有默认分组编号的组另外再给一个别名
    # (?P<name>正则表达式)#name是一个合法的标识符
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]