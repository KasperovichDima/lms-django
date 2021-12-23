from datetime import date
from random import choice

from django.db import models

from faker import Faker


class Group(models.Model):

    group_name = models.CharField(max_length=30)
    start_date = models.DateField(default="19.10.2021")
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headman_in_group'
    )
    teachers = models.ManyToManyField(
        to='teachers.Teacher',
        related_name='groups'
        )

    def __str__(self):
        return f'{self.group_name} - {self.start_date}'

    @classmethod
    def create_group(Group):
        fk = Faker()
        letter = choice(['A', 'B', 'C', 'D'])
        number = choice(['1', '2', '3', '4'])
        obj = Group(group_name=(letter + number),
                    start_date=fk.date_between_dates(date(2021, 1, 10), date(2021, 12, 25)))

        obj.save()
        return obj

    @staticmethod
    def headman_chooser():
        for _ in Group.objects.all():
            try:
                _.headman = choice(list(_.students.all()))
                _.save()
            except IndexError:
                continue
