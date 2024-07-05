from django.db import models
# Create your models here.


class TODO(models.Model):
    task_title = models.CharField(max_length=100, default='')
    task_description = models.CharField(max_length=500,  default='')
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']
