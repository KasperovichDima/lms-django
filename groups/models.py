from django.db import models


class Group(models.Model):

    course_name = models.CharField(max_length=30)
    start_date = models.DateField(default="19.10.2021")
    number_of_students = models.IntegerField()
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}, {self.start_date}, ' \
               f'{self.number_of_students}, {self.teacher_name}'
