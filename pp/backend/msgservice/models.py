from django.db import models
from django import forms

# Create your models here.
class MsgService(models.Model):
    email_id = models.EmailField(max_length=30)
    mobile_no = models.CharField(max_length=12)
