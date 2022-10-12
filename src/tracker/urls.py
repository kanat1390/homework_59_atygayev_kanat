from django.urls import path
from .views import (
    ProjectListView, 
    ProjectDetailView,
    TaskDetailView,
    ProjectCreateView,
    TaskCreateView,
    TaskListView,
    )

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/create/', TaskCreateView.as_view(), name='task-create'),
    
]