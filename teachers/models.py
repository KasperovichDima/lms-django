from django.db import models
import random
from core.models import Person
from groups.models import Group



class Teacher(Person):

    salary = models.PositiveIntegerField(default=1500)
    specialization = models.CharField(max_length=100)
    work_experience = models.IntegerField(null=True)
    # group = models.ManyToManyField(
    #     to='groups.Group',
    #     related_name='teacher'
    # )

    @classmethod
    def _generate(cls, group):
        teacher = super()._generate(group)
        teacher.salary = random.randint(1500, 3500)
        teacher.specialization = random.choice(['Python', 'Java', 'JS', 'C/C++', 'cobol', 'basic'])
        teacher.work_experience = random.randrange(5, 15)
        teacher.groups.add(group)

        teacher.save()
