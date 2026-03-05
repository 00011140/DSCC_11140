from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

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