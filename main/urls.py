from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('apply', views.apply, name="apply"),
    path('send_apply', views.send_apply, name="send_apply"),
    path('manage', views.manage, name="manage")
]