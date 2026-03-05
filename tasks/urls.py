from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    # path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    # path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    # path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    # path('register/', views.RegisterView.as_view(), name='register'),
]