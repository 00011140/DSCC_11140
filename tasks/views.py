from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})

class TaskListView(ListView):
    model = Task
    template_name = "tasks/home.html" 
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "completed", "project", "tags"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "completed", "project", "tags"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("home")

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")  