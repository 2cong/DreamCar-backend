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

# drive_contact_channel
CSV_PATH = './CSV/drive_contact.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        DriveContactChannel.objects.create(
            email = row['email'],
            fax   = row['fax'],
            mail  = row['mail'],
            sms   = row['sms'],
            call  = row['call'],
            sns   = row['sns']
        )

# expectdate
CSV_PATH = './CSV/ExpectDate.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        ExpectDate.objects.create(
            period= row['period']
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
            phone_number = row['phone_number'],
            address_city = AddressCity.objects.get(id=row['address_city_id']),
            address_detail = row['address_detail'],
            email = row['email'],
            gender = Gender.objects.get(id=row['gender_id']),
            drive_contact_channel = DriveContactChannel.objects.get(id=row['drive_contact_channel']),
            privacy_check = row['privacy_check']
        )

# test_drive_schedule_
CSV_PATH = './CSV/test_driver_schedule.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        TestDriveSchedule.objects.create(
            model_version_line = ModelVersionLine.objects.get(id = row['mvl']),
            store_information = StoreInformation.objects.get(id =row['store']),
            expect_date = ExpectDate.objects.get(id = row['expect']),
            contact_us = row['contact'] 
        )

# test_drive
CSV_PATH = './CSV/test_drive.csv'
   
with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        TestDrive.objects.create(
            test_drive_schedule = TestDriveSchedule.objects.get(id = row['schedule']),
            user = User.objects.get(id = row['user']),
            current_car_model = row['current_car']
        )

