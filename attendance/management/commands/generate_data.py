from django.core.management.base import BaseCommand
from attendance.models import UsersAttendance
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate 1,000,000 records for YourModel'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10000):
            UsersAttendance.objects.create(
                date=fake.date_this_decade(),
                is_present=random.randint(0, 1),
                direction_id=random.randint(1, 2),
                profile_id=random.randint(1, 2)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 1,000,000 records'))
