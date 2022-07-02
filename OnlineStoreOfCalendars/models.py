from unicodedata import name
from django.db import models

class CATEGORY(models.Model):
    name=models.CharField(max_length=25)

class LANGUAGE(models.Model):
    name=models.CharField(max_length=10)
    id_name=models.CharField(max_length=3)

class CALENDAR(models.Model):
    name=models.CharField(max_length=25)
    icon=models.ImageField(default="static/DC_Comics_logo.png")
    category=models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    check_mark=models.BooleanField(default=False)
    password=models.CharField(max_length=20)
    author=models.CharField(max_length=15, default="None")
    calendarID=models.CharField(max_length=80)
    description=models.TextField()
    language=models.ForeignKey(LANGUAGE,on_delete=models.CASCADE)
    likes=models.PositiveIntegerField(default=0)
