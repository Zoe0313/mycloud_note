from django.shortcuts import render
from . import models

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

def mylogin(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username','')
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        # 获取表单数据
        remember = request.POST.get('remember','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        print(username+password)

        # 验证用户名、密码是否正确
        try:
            user = models.User.objects.get(name=username,password=password)
            request.session['userinfo'] = {
                'username': user.name,
                'id': user.id,
            }
        except:
            return HttpResponse('登录失败')

        # 处理cookies
        resp = HttpResponseRedirect('/')#登录成功返回首页
        if remember:
            resp.set_cookie('username',username,7*24*3600)
        else:# 记住密码不选中就是一个空字符串
            resp.delete_cookie('username')
        return resp

def myregister(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        if username == '':
            username_error = '用户名不能为空'
            return render(request, 'user/register.html', locals())
        elif password == '':
            password_error = '密码不能为空'
            return render(request, 'user/register.html', locals())
        elif password != password2:
            password2_error = '两次密码输入不一致'
            return render(request, 'user/register.html', locals())

        # 开始注册功能
        try:
            user = models.Users.objects.create(
                name=username,
                password=password
            )
            return HttpResponse('注册成功')
        except:
            return HttpResponse('注册失败')

def mylogout(request):
    # 退出主页
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/')# 注销后跳转到主页