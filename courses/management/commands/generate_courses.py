from random import choice

from courses.models import Course

from django.core.management.base import BaseCommand

from groups.models import Group


class Command(BaseCommand):
    help = 'generates [count (def = 10)] random courses and groups and saves them to db'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            default=10,
            type=int,
            dest='count'
        )

    def handle(self, *args, **options):
        for _ in range(options['count']):
            group = Group.create_group()
            course = Course(
                course_name=choice(['UX/UI', 'Backend', 'Frontend',
                                             'Gamedev', 'Enterprise', 'OSdev']),
                start_date=group.start_date,
                group=group
            )
            course.save()
