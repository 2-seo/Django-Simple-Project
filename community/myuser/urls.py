from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register) # views.py에 있는 register라는 함수
]