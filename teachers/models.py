from django.db import models


class Teacher(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    specialization = models.CharField(max_length=100)
    work_experience = models.IntegerField()
