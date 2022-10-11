from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(to='tracker.Project', on_delete=models.CASCADE)
    status = models.ForeignKey(to='tracker.Status', on_delete=models.PROTECT)
    types = models.ManyToManyField('tracker.Type', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
