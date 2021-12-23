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
        fk = Faker()
        for _ in range(options['count']):
            letter = choice(['A', 'B', 'C', 'D'])
            number = choice(['1', '2', '3', '4'])
            gr = gm.Group(group_name=(letter + number),
                          start_date=fk.date_between_dates(date(2021, 1, 10), date(2021, 12, 25)),
                          )
            gr.save()
