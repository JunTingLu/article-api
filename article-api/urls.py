"""article-api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# 當 training_slash 為 True 時，在服務器啟動的網址後會自動加上 "\" 
router = DefaultRouter(trailing_slash=False)
# 將 view 中定義的 ArticleViewSet 映射至 url，並重新導向到 127.0.0.1:8000/api/articles 
router.register('articles', views.ArticleViewSet, basename='article')

urlpatterns = [
    # 管理者相關端點
    url('admin/', admin.site.urls),
    # 其他所有端點
    url('api/', include(router.urls)),
    # 取得 token 端點
    path('api/token', TokenObtainPairView.as_view(), name='obtain_token'),
    # 刷新 token 端點
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    # 驗證 token 端點
    path('api/token/verify', TokenVerifyView.as_view(), name='verify_token'),
]
