from random import choice, randint

from django.core.management.base import BaseCommand

from faker import Faker

import teachers.models as tm


class Command(BaseCommand):
    help = 'generates [count (def = 10)] random teachers ans saves them to db'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            default=10,
            type=int,
            dest='count'
        )

    def handle(self, *args, **options):
        for _ in range(options['count']):
            fk = Faker()
            t = tm.Teacher(first_name=fk.first_name(),
                           last_name=fk.last_name(),
                           age=fk.pyint(25, 75),
                           specialization=choice(['C/C++', 'JAVA', 'JS', 'Python', 'PHP', 'Rust']),
                           work_experience=randint(2, 30))
            t.save()
