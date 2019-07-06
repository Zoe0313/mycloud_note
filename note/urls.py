from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r"^all", views.showall),
    url(r"^new", views.new), # 新建笔记
    url(r"^del/(\d+)", views.delete), # 删除笔记
    url(r"^mod/(\d+)", views.modify), # 修改笔记
]