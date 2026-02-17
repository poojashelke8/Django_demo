from django.db import models
from django.utils import timezone

# Create your models here.
class Details_Demo(models.Model):
    DEMO_INFO=[
        ('FR','FRONTEND'),
        ('BC','BACKEND'),
        ('DT','DATA'),
    ]
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='demoImage/')
    date_added = models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=DEMO_INFO)
    description = models.TextField(default='')
    is_published = models.BooleanField(default=False)