from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.detailedView, name='DetailedView'),
    path('task-create/', views.taskCreate, name='Create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='Update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='Delete'),
]
