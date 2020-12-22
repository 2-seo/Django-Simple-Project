from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),  # views.py에 있는 register 함수
    path('login/', views.login),
    path('logout/', views.logout)
]
