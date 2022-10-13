from django.urls import path
from .views import (
    ProjectListView, 
    ProjectDetailView,
    TaskDetailView,
    ProjectCreateView,
    TaskCreateView,
    TaskListView,
    ProjectUpdateView,
    )

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
]