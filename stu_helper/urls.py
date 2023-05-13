"""stu_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # 后端rest接口
    path('main/', include('main.urls')),

    # / -> 管理后台
    path('', RedirectView.as_view(url='/admin/')),
    path('admin/', admin.site.urls),

    # rest认证，
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # DRF 接口文档
    # path('api/', include_docs_urls(title='DRF API 文档', description='校园助手API')),
]
