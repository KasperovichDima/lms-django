from django.db import models


class Group(models.Model):

    cours_name = models.CharField(max_length=30)
    start_date = models.DateField(default="19.10.2021")
    number_of_students = models.IntegerField()
    teacher_name = models.CharField(max_length=50)
