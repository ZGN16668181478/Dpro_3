from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showContent(request,num):
    return render(request,'myApp/grades.html')

def showGrades(request):

    from .models import grades
    gradesList = grades.gObj.all()
    return render(request,'myApp/grades.html',{'gradesList':gradesList})

def showStudent(request):
    from .models import students
    studentList = students.stuObj2.all()
    return render(request,'myApp/students.html',{'studentList':studentList})

def showStudents(request,num):
    from .models import grades,students
    idList = grades.objects.get(gId=num)
    print(idList)
    studentsList = idList.student_set.all()
    return render(request,'myApp/students.html',{'studentsList':studentsList})

def addStudents(request):
    from .models import students,grades
    grade = grades.gObj.get(gNum=10)
    stu = students.createStudents('肖恩蒙德兹',11,True,'1992-01-08',grade,'2019-03-06','2019-2-3','2019-03-07')
    stu.save()
    return HttpResponse(stu)
    # return HttpResponse('xxxx')

def showregist(request):

    return render(request,'myApp/form.html')

def regist(request):
    userName = request.GET.get('userName')
    sex = request.GET.get('gender')
    hobbies = request.GET.getlist('hobby')
    print(userName,sex,[hobby for hobby in hobbies])
    print(request.GET)
    # return HttpResponse(userName,sex,[hobby for hobby in hobbies])
    return HttpResponse('Oh shit mother fucker!')

def showreponse(request):
    # 没有reponse对象，需要自己创建一个对象
    res = HttpResponse()
    charset = res.charset
    content = res.content
    status_code = res.status_code
    cookies = res.cookies
    print(charset,content,status_code,cookies)
    return HttpResponse('This is my Reponse test page！')

def setCookie(request):
    res = HttpResponse()
    # r = res.set_cookie('name','zhangguinan')
    # # 将响应里写入数据
    r = request.COOKIES
    r2 =  res.write('<h1>'+r['name']+'</h1>')
    # 这里是写入到响应里，返回值直接为响应
    return res

#重定向  可以处理一些重复操作，比如数据库的一些操作   这里的post请求会发生错误！！！
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def showRedirect(request):
    return redirect('showredirect2/')
def showRedirect2(request):
    return HttpResponse('This is my Redirect Page!')

# 存储状态session   这里利用重定向存储session
def showHome(request):
    userName = request.session.get('name', '妈卖批')
    print('showHome is running!')
    return render(request,'myApp/home.html',{'userName':userName})
def showLogin(request):
    # print('login is running!')
    # userName = request.POST.get('userName')
    # request.session['userName'] = userName
    # return redirect('/showLogin')
    return render(request,'myApp/login.html')
def loginTo(request):
    print('loginto is running!')
    userName = request.GET.get('userName')
    print(userName)
    request.session['userName'] = userName
    print(request.session['userName'])
    return redirect('/loginTo')
def LoginToHome(request):
    userName = request.session.get('userName', '妈卖批')
    print(userName,'is running!')
    return render(request,'myApp/home.html',{'userName':userName})
# 使用logout模块清除session
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('/loginTo')

def test_module(request):

    return render(request,'myApp/test.html')

def test_good(request):
    print('test_good is running!')
    return render(request,'myApp/good.html')

def good_num(request):
    return HttpResponse('Sunck is a goodMan!')

def showExtends(request):
    content = '<h1>Oh shit Mother Fucker!</h1>'
    return render(request,'myApp/showExtends.html',{'content':content})

def verifyCode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色，宽，高
    bgcolor = (random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width,height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔对象的point()函数绘制噪点
    for x in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str = '123456789!@#$%^&*QWERTYUIOPASDFGHJKZXCVBNM'
    # 随机选取四个值作为验证码

    rand_str = ''
    for i in range(0,4):
        rand_str += str[random.randrange(0,len(rand_str))]
    # 构造字体对象 默认即可
    # 构造字体颜色
    fontcolor1 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor2 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor3 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor4 = (255,random.randrange(0,255),random.randrange(0,255))
    # 释放画笔
    del draw
    # 存入session, 用作下一步验证
    request.session['verifyCode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf,'png')
    # 将内存中的图片返回客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')