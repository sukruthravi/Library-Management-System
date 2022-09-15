import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django

django.setup()

##FAKE POP SCRIPT

import random

from AppTwo.models import *
from faker import Faker

fakegen = Faker()

def populate(N=5):

	for entry in range(N):

		fake_firstname = fakegen.first_name()
		fake_latname = fakegen.last_name()
		fake_email = fakegen.email()

		usr = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_latname,email=fake_email)[0]


if __name__ == '__main__':
	print("Adding users: populating")
	populate(20)
	print("Users added. populating complete")