from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path("accounts/login/", LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path('create/', views.create_task, name='create_task'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    # path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    # path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    # path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    # path('register/', views.RegisterView.as_view(), name='register'),
]