from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from backend import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^users$', views.user_index, name="user_index"),    
]