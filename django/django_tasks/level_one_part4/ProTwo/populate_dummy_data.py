import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django

django.setup()

from faker import Faker
from AppTwo.models import *

faker_gen = Faker()

def populate(N = 5):

    for entry in range(N):

        user = User.objects.get_or_create(first_name = faker_gen.first_name(), last_name = faker_gen.last_name(), email = faker_gen.email())[0]
        user.save()

if __name__ == "__main__":

    print("Populating User start")
    populate(20)
    print("Populating user completed")
