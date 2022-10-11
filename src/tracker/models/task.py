from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(to='tracker.Status', on_delete=models.PROTECT)
    types = models.ForeignKey(to='tracker.Type', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
