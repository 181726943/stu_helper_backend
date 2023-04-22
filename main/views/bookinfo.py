from django.shortcuts import render


def bookinfo(request):
    return render(request, "bookinfo.html")