from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank = True)
    date_posted = models.DateTimeField(default=timezone.now)
    