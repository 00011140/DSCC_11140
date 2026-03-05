from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/home.html", {"tasks": tasks})

@login_required
def create_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks:home")

    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


