import csv
import os
import django
import sys

os.chdir(".")
print("Currnet dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from shopping.models import *

# gender
CSV_PATH = './CSV/gender.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Gender.objects.create(
            name = row['gender']
        )

# Store_information
CSV_PATH = './CSV/store_information.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        StoreInformation.objects.create(
            name = row['store_name'],
            address = row['store_address'],
            city = row['city'],
            service_center = row['service_center'],
            exhibition_center = row['exhibition_center'],
            telephone = row['telephone'],
            fax = row['fax'],
            description1 = row['description1'],
            description2 = row['description2']
        )

# address_city
CSV_PATH = './CSV/addresscity.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        AddressCity.objects.create(
            city = row['city']
        )

# user
CSV_PATH = './CSV/user.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        User.objects.create(
            first_name = row['first_name'],
            last_name = row['last_name'],
            birthday = row['birthday'],
            phonenumber = row['phone_number'],
            address_city = AddressCity.objects.get(id=row['address_city_id']),
            address_detail = row['address_detail'],
            email = row['email'],
            gender = Gender.objects.get(id=row['gender_id'])
        )
