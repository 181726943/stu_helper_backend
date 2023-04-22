from django.shortcuts import render


def personalinfo(request):
    """编辑/查看个人信息"""
    if request.method == "GET":
        pass
    return render(request, 'personalinfo.html')