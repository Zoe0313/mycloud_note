from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r"^login", views.mylogin),
    url(r"^logout", views.mylogout),
    url(r"^reg", views.myregister),
]