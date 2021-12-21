from django.db import models
import random
from core.models import Person
from groups.models import Group



class Teacher(Person):

    salary = models.PositiveIntegerField(default=1500)
    specialization = models.CharField(max_length=100)
    work_experience = models.IntegerField(null=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers'
    )

    @classmethod
    def _generate(cls, *args, **kwargs):
        teacher = super()._generate( *args, **kwargs)
        teacher.salary = random.randint(1500, 3500)
        teacher.specialization = random.choice(['Python', 'Java', 'JS', 'C/C++', 'cobol', 'basic'])
        teacher.work_experience = random.randrange(5, 15)

        teacher.save()
