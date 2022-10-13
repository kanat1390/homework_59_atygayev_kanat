from django.db import models
from django.urls import reverse


class Project(models.Model):
    started_date = models.DateField()
    finished_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    
        
