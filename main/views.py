from django.shortcuts import render, redirect
from main.models import score, bookinfo


# Create your views here.

def home(request):

    return render(request, "home.html")
