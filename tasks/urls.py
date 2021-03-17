from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category_list'),
    path('show_category/<str:pk>/', views.show_category, name='show_category'),
    path('update/<str:page>/<str:pk>/', views.updateTask, name="update"),
    path('delete_task/<str:page>/<str:pk>/', views.deleteTask, name="delete_task"),
    path('create_task/<str:page>/', views.createTask, name="create_task"),
]