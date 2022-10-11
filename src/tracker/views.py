from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tracker.models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/project_detail.html'


