from django.db import models

# Create your models here.


class News(models.Model):
    heading = models.CharField(max_length=90)
    news = models.TextField()
    date = models.DateTimeField(auto_now=True)

