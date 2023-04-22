from io import BytesIO

from django import forms
from django.shortcuts import render, redirect, HttpResponse

from main import models
from main.utils.auth_code import check_code
from main.utils.bootstrap import BootStrapForm
from main.utils.encrypt import md5


class LoginForm(BootStrapForm):
    stu_num = forms.CharField(
        label="学号/工号",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True
    )
    img_code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return md5(password)


def login(request):
    """登录"""
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    login_form = LoginForm(data=request.POST)
    if login_form.is_valid():
        # 验证成功，获取到用户名和密码
        # {'username': '222019603193109', 'password': '73a2dbba1d86b839a332fb4496c7894f'}
        # print(login_form.cleaned_data)
        # 校验验证码
        user_input_code = login_form.cleaned_data.pop('img_code')
        right_code = request.session.get("img_code", "")
        if user_input_code.lower() != right_code.lower():
            login_form.add_error("img_code", "验证码错误")
            return render(request, 'login.html', {"login_form": login_form})

        # 数据库校验,获取用户对象、None
        # user_obj = models.UserInfo.objects.filter(username=login_form.cleaned_data['username'],
        # password=login_form.cleaned_data['password']).first()

        user_obj = models.UserInfo.objects.filter(**login_form.cleaned_data).first()
        if not user_obj:
            login_form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'login_form': login_form})

        # 用户名或密码正确
        # 网站生成随机校验码，写入用户浏览器cookie中，写入session中
        # 写入单个数据
        # request.session["info"] = user_obj.stu_num

        # 写入多个数据
        request.session["info"] = {'stu_num': user_obj.stu_num, 'name': user_obj.user}
        # 设置session有效时间，即免登录时长
        request.session.set_expiry(60 * 60 * 24)
        return redirect("/main/home/")

    return render(request, 'login.html', {'login_form': login_form})


def image_code(request):
    """生成图形验证码"""
    # 调用pillow函数，生成图形验证码
    img, img_code = check_code()
    # 写入当前用户session中
    request.session['img_code'] = img_code
    # 设置session超时
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')
