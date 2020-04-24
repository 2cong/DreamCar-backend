from django.db 		import models
from car.models		import ModelVersionLine

class User(models.Model):
    first_name     = models.CharField(max_length = 200)
    last_name      = models.CharField(max_length = 200)
    birthday       = models.DateField()
    phonenumber    = models.CharField(max_length = 200)
    address_city   = models.OneToOneField('AddressCity', on_delete = models.SET_NULL, null = True)
    address_detail = models.CharField(max_length = 1000)
    email          = models.EmailField(max_length = 200)
    gender         = models.OneToOneField('Gender', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'users'

class AddressCity(models.Model):
    city  = models.CharField(max_length = 50)

    class Meta:
        db_table = 'address_citise'

class Gender(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'genders'

class TestDrive(models.Model):
    test_drive_schedule  = models.ForeignKey('TestDriveSchedule', on_delete = models.SET_NULL, null = True)
    user                 = models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    current_car_model    = models.CharField(max_length = 50)

    class Meta:
        db_table = 'test_drives'

class TestDriveSchedule(models.Model):
    model_version_line  = models.ForeignKey('car.ModelVersionLine', on_delete = models.SET_NULL, null = True)
    store_information   = models.ForeignKey('StoreInformation', on_delete = models.SET_NULL, null = True)
    expect_date         = models.ForeignKey('ExpectDate', on_delete = models.SET_NULL, null = True)
    contact_us          = models.TextField()

    class Meta:
        db_table = 'test_drive_schedules'

class ExpectDate(models.Model):
    period  = models.CharField(max_length = 100)

    class Meta:
        db_table = 'expect_dates'

class StoreInformation(models.Model):
    name        = models.CharField(max_length = 50)
    address     = models.CharField(max_length = 1000)
    city              = models.CharField(max_length = 50)
    service_center    = models.BooleanField()
    exhibition_cneter = models.BooleanField()
    telephone         = models.CharField(max_length = 50)
    fax               = models.CharField(max_length = 50)
    description1      = models.CharField(max_length = 2000)
    description2      = models.CharField(max_length = 2000)

    class Meta:
        db_table = 'store_informations'
