from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()
    location = models.TextField()
    rank = models.IntegerField()
    review = models.TextField()
    courses = models.ForeignKey('Courses', on_delete=models.CASCADE)
class Courses(models.Model):
    name = models.CharField(max_length=30)
    duration= models.IntegerField()
    type_of_course = models.CharField(max_length=30)
    resource = models.TextField()

class Exam(models.Model):
    name = models.CharField(max_length=30)
    college_name = models.ForeignKey('College', on_delete=models.CASCADE)
    exam_date = models.DateField(auto_now=False)
    date = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
