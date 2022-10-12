from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from tracker.models import Project, Task, status
from django.urls import reverse
from tracker.forms import SearchForm

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
        print(text)
        task_list = self.model.objects.all()
        if text:
            task_list = task_list.filter(summary__icontains=text)
        return task_list
    


class TaskDetailView(DetailView):
    model = Task
    template_name: str = 'tracker/task_detail.html'


class ProjectCreateView(CreateView):
    model = Project
    fields = ['started_date', 'finished_date', 'name', 'description']
    template_name = 'tracker/forms/project_form.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['summary', 'description', 'status', 'types']
    template_name = 'tracker/forms/task_form.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        return super().form_valid(form)


