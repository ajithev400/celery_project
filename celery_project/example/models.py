from email.policy import default
from django.db import models

# Create your models here.

class Celery_log(models.Model):
    file_name = models.CharField(max_length=50,blank=True,null=True)
    count = models.CharField(max_length=10,blank=True,null=True)
    task_id = models.CharField(max_length=30,blank=True,null=True)
    status = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self) :
        return self.file_name