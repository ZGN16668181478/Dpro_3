from django.conf.urls import url
from django.urls import re_path,path

from myApp import views
urlpatterns = [
    # 使用这种匹配好像是有关于这个的path都不可少，缺少就500
    re_path('^test/$',views.test_module),
    # url直接是引号里所有，对于/d没匹配到的另外加上  eg:{% url 'test：good' 1 %}
    # re_path(r'^good/(\d+)/$',views.good_num,name='good'),
    re_path(r'^good/(\d+)/$',views.test_good,name='good'),
    # re_path('(\d+)/',show),
    # re_path('(\S+)/',showContent),
    re_path(r'grades/',views.showGrades),
    re_path(r'students/$',views.showStudent),
    re_path(r'^grades/(\d+)',views.showStudents),
    re_path(r'addStudents/',views.addStudents),
    re_path(r'^showregist/$',views.showregist),
    re_path(r'^showregist/regist/',views.regist),
    re_path(r'^response/$',views.showreponse),
    re_path(r'^cookie/$',views.setCookie),
    re_path(r'^showredirect/$',views.showRedirect),
    re_path(r'^showredirect2/$',views.showRedirect2),
    re_path(r'^home/',views.showHome),
    re_path(r'^login/',views.showLogin),
    re_path(r'^showLogin/',views.loginTo),
    re_path(r'^loginTo/',views.LoginToHome),
    # re_path(r'^loginToHome/',LoginToHome),
    re_path(r'^quit/',quit),
    re_path(r'^showExtends/',views.showExtends)
    ]