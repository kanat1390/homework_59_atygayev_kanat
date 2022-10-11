from django.shortcuts import render
from django.views.generic import ListView
from tracker.models import Project

class ProjectListView(ListView):
    model = Project


