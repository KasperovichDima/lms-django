from datetime import date
from random import choice

from django.core.management.base import BaseCommand

from faker import Faker

import groups.models as gm


class Command(BaseCommand):
    help = 'generates [count (def = 10)] random groups ans saves them to db'  # noqa

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
            t = gm.Group(course_name=choice(['C/C++', 'JAVA', 'JS', 'Python', 'PHP', 'Rust']),
                         start_date=fk.date_between_dates(date(2021, 1, 10), date(2021, 12, 25)),
                         number_of_students=fk.pyint(5, 25),
                         teacher_name=fk.name())
            t.save()
