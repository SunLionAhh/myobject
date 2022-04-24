# 会员移动端子路由文件
from django.urls import path
from mobile.views import index

urlpatterns = [
    path('', index.index, name="mobile_index"),
]
