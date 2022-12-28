from django.urls import path
from myfirstpage import views

urlpatterns = [
    path("", views.home, name="home"),
]