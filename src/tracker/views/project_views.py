from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tracker.models import Project
from django.urls import reverse
from tracker.forms import ProjectForm
from django.core.paginator import Paginator
from .mixin import SuccessDetailUrlMixin


class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/project_list.html'
    ordering = ['-started_date']


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['project'].tasks.all()
        paginator = Paginator(tasks, per_page=6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class ProjectCreateView(SuccessDetailUrlMixin, CreateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание проекта'
        return context


class ProjectUpdateView(SuccessDetailUrlMixin, UpdateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование проекта'
        return context


class ProjectDeleteView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('project-list')