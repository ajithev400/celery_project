from email.policy import default
from django.db import models

# Create your models here.
CHOICES ={
    ('success','success'),
    ('failed','failed'),
    ('pending','pending'),
    ('running','running')
}
class Celery_model(models.Model):
    task_id = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=CHOICES,default='pending')