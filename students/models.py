from django.db import models
from faker import Faker
from django.http import HttpResponse


class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'

    @staticmethod
    def generate_students(request):
        """
        generates random students and saves them to db
        :param request: url parameter 'count'
        default = 10
        :return:
        """
        num = 10  # default number of students to generate

        if 'count' in request.GET:
            if request.GET['count'].isdigit():
                num = int(request.GET['count'])

        fake = Faker()
        for _ in range(num):
            std = Student(first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          age=fake.pyint(15, 75))
            std.save()

        http = f'<h1>{num} students generated!</h1>'
        return HttpResponse(http)