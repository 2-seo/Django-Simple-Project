from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_wirte),
    path('detail/<int:pk>/', views.board_detail)
]