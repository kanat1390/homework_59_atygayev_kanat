from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from tracker.models import Project, Task, status
from django.urls import reverse
from tracker.forms import SearchForm
from tracker.forms import ProjectForm

class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/project_detail.html'

class TaskListView(ListView):
    model = Task
    template_name = 'tracker/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search_form'] = search_form
        return context
    
    def get_queryset(self):
        text = self.request.GET.get('text', '')
        task_list = self.model.objects.all()
        if text:
            task_list = task_list.filter(summary__icontains=text)
        return task_list
    


class TaskDetailView(DetailView):
    model = Task
    template_name: str = 'tracker/task_detail.html'

class SuccessDetailUrlMixin:
    detail_url_name = None 
    def get_success_url(self):
        return  reverse(self.detail_url_name, kwargs={'pk':self.object.pk})

class ProjectCreateView(SuccessDetailUrlMixin, CreateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание проекта'
        return context
    

class TaskCreateView(SuccessDetailUrlMixin, CreateView):
    model = Task
    fields = ['summary', 'description', 'status', 'types']
    template_name = 'tracker/forms/task_form.html'
    detail_url_name = 'task-detail'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        return super().form_valid(form)

class ProjectUpdateView(SuccessDetailUrlMixin, UpdateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование проекта'
        return context



