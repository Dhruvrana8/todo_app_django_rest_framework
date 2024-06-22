from django.db import models
# Create your models here.


class TODO(models.Model):
    task=models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    is_completed= models.BooleanField(default=False)
    is_deleted= models.BooleanField(default=False)