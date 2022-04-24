# 前台大堂点餐端子路由文件
from django.urls import path
from web.views import index

urlpatterns = [
    path('', index.index, name="web_index"),
]
