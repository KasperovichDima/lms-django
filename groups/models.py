from django.db import models


class Group(models.Model):

    course_name = models.CharField(max_length=30)
    start_date = models.DateField(default="19.10.2021")
    number_of_students = models.IntegerField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headman_in_group'
    )
    teacher = models.ManyToManyField(
        to='teachers.Teacher',
        related_name='groups'
    )

    def __str__(self):
        return f'{self.course_name} - {self.start_date}'
#              f'{self.number_of_students}, {self.teacher_name}'
