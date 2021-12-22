from datetime import date
from datetime import timedelta

from core.models import Person

from django.db import models

from groups.models import Group


class Student(Person):
    enroll_date = models.DateField(default=date.today)
    graduate_date = models.DateField(null=True)
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def save(self, *args, **kwargs):
        self.enroll_date = self.group.start_date
        self.graduate_date = self.enroll_date + timedelta(days=120)
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls, group):
        student = super()._generate()
        student.enroll_date = group.start_date
        student.graduate_date = student.enroll_date + timedelta(days=120)
        student.group = group

        student.save()

    # @staticmethod
    # def generate_students(request):
    #     """
    #     generates random students and saves them to db
    #     :param request: url parameter 'count'
    #     default = 10
    #     :return:
    #     """
    #     num = 10  # default number of students to generate
    #
    #     if 'count' in request.GET:
    #         if request.GET['count'].isdigit():
    #             num = int(request.GET['count'])
    #
    #     fake = Faker()
    #     group = Group.objects.all()
    #
    #     for _ in range(num):
    #         birthday = fake.date_between_dates(date(1970, 1, 1), date(2000, 1, 1))
    #         enroll_date = fake.date_between_dates(date(2021, 10, 1), date.today())
    #
    #         std = Student(first_name=fake.first_name(),
    #                       last_name=fake.last_name(),
    #                       birthday=birthday,
    #                       # age=date.today() - birthday,
    #                       group=random.choice(group),
    #                       enroll_date=enroll_date,
    #                       graduate_date=enroll_date+timedelta(days=120),
    #                       phone_number='380' + f'{random.choice([50,95,67,97,63,73])}' +
    #                                    f'{random.choice(range(1000000,9999999))}'
    #                       )
    #         std.save()
    #
    #     return f'{num} students generated!'
