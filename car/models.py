from django.db import models

class Model(models.Model):
    name         = models.CharField(max_length = 50)

    class Meta:
        db_table = 'models'


class Version(models.Model):
    name         = models.CharField(max_length = 50)

    class Meta:
        db_table = 'versions'


class Line(models.Model):
    name         = models.CharField(max_length = 50)

    class Meta:
        db_table = 'lines'


class ModelVersionLine(models.Model):
    model         = models.ForeignKey('Model', on_delete = models.SET_NULL, null = True)
    version       = models.ForeignKey('Version', on_delete = models.SET_NULL, null = True)
    line          = models.ForeignKey('Line', on_delete = models.SET_NULL, null = True)
    sepc          = models.ForeignKey('Spec', on_delete = models.SET_NULL, null = True)
    dimension     = models.ForeignKey('Dimension', on_delete = models.SET_NULL, null = True)


    class Meta:
        db_table  = 'model_version_lines'


class Spec(models.Model):
    acceleration    = models.DecimalField(max_digits = 10, decimal_places = 2)
    max_speed       = models.IntegerField(default = 0)
    displacement    = models.IntegerField(default = 0)
    max_torque      = models.IntegerField(default = 0)
    max_power       = models.IntegerField(default = 0)
    engine_layout   = models.CharField(max_length = 50)
    engine_stroke   = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        db_table    = 'specs'


class Dimension(models.Model):
    length              = models.IntegerField(default = 0)
    width_side          = models.IntegerField(default = 0)
    width_noside        = models.IntegerField(default = 0)
    height              = models.IntegerField(default = 0)
    wheelbase           = models.IntegerField(default = 0)
    front_track         = models.IntegerField(default = 0)
    rear_track          = models.IntegerField(default = 0)
    front_overhang      = models.IntegerField(default = 0)
    rear_overhang       = models.IntegerField(default = 0)
    turning_circle      = models.DecimalField(max_digits = 10, decimal_places = 2)
    boot_capacity       = models.IntegerField(default = 0)
    fuel_tank_capacity  = models.IntegerField(default = 0)
    unladen_weight      = models.IntegerField(default = 0)
    kerb_weight         = models.IntegerField(default = 0)
    tire_size_front     = models.CharField(max_length = 50)
    tire_size_back      = models.CharField(max_length = 50)

    class Meta:
        db_table        = 'dimensions'



class CustomCar(models.Model):
    model_version_line  = models.ForeignKey('ModelVersionLine', on_delete=models.SET_NULL, null=True)
    exterior_group      = models.ForeignKey('ExteriorGroup',on_delete=models.SET_NULL, null=True)
    interior_group      = models.ForeignKey('InteriorGroup', on_delete=models.SET_NULL, null=True)
    customcar_accessory  = models.ManyToManyField('Accessory', through='CustomCarAccessory')
    package             = models.ManyToManyField('Package', through='ModelVersionLinePackage')

    class Meta:
        db_table        = 'customcars'


class CustomCarProfile(models.Model):
    custom_car   = models.OneToOneField('CustomCar',on_delete=models.SET_NULL, null=True)
    name         = models.CharField(max_length=200)
    email        = models.EmailField(max_length=200)
    code         = models.CharField(max_length=400)

    class Meta:
        db_table = 'customcarprofiles'


class Color(models.Model):
    name         = models.CharField(max_length=100)

    class Meta:
        db_table = 'colors'


class CustomCarAccessory(models.Model):
    custom_car    = models.ForeignKey('CustomCar',on_delete=models.SET_NULL,null=True)
    accessory     = models.ForeignKey('Accessory',on_delete=models.SET_NULL, null=True)
    quantity      = models.IntegerField(default=0)

    class Meta:
        db_table  = 'customcaraccessories'


class Accessory(models.Model):
    name          = models.CharField(max_length=100)
    category      = models.ForeignKey('AccessoryCategory',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table  = 'accessories'


class AccessoryCategory(models.Model):
    category     = models.CharField(max_length=100)

    class Meta:
        db_table = 'accessorycategories'


class ModelVersionLinePackage(models.Model):
    model_version_line   = models.ForeignKey('ModelVersionLine', on_delete=models.SET_NULL, null=True)
    package              = models.ForeignKey('Package',on_delete=models.SET_NULL, null=True)
    custom_car           = models.ForeignKey('CustomCar',on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table         = 'modelversionlinepackages'


class Package(models.Model):
    name         = models.CharField(max_length=100)
    list1        = models.CharField(max_length=500)
    list2        = models.CharField(max_length=500)
    list3        = models.CharField(max_length=500)
    list4        = models.CharField(max_length=500)

    class Meta:
        db_table = 'packages'



class ExteriorGroup(models.Model):
    exterior     = models.ForeignKey('Exterior', on_delete=models.SET_NULL, null= True)
    wheel        = models.ForeignKey('Wheel', on_delete=models.SET_NULL, null=True)
    caliper      = models.ForeignKey('Caliper', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'exteriorgroups'


class Exterior(models.Model):
     model_version_line = models.ForeignKey('ModelVersionLine', on_delete=models.SET_NULL, null=True)
     exterior_type      = models.ForeignKey('ExteriorType',on_delete=models.SET_NULL, null=True)
     code               = models.CharField(max_length=100)

     class Meta:
         db_table       = 'exteriors'


class ExteriorType(models.Model):
    color           = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    thumnail_url    = models.URLField(max_length=2000)

    class Meta:
        db_table    = 'exteriortypes'


class Wheel(models.Model):
    model_version_line  = models.ForeignKey('ModelVersionLine', on_delete=models.SET_NULL, null=True)
    wheel_type          = models.ForeignKey('WheelType',on_delete=models.SET_NULL, null=True)
    code                = models.CharField(max_length=100)

    class Meta:
        db_table        = 'wheels'


class WheelType(models.Model):
    name            = models.CharField(max_length=100)
    thumnail_url    = models.URLField(max_length=2000)

    class Meta:
        db_table    = 'wheeltypes'


class Caliper(models.Model):
    model_version_line  = models.ForeignKey('ModelVersionLine',on_delete=models.SET_NULL, null=True)
    caliper_type        = models.ForeignKey('CaliperType', on_delete=models.SET_NULL, null=True)
    code                = models.CharField(max_length=100)

    class Meta:
        db_table        = 'calipers'


class CaliperType(models.Model):
    color           = models.ForeignKey('Color', on_delete=models.SET_NULL,null=True)
    thumnail_url    = models.URLField(max_length=2000)

    class Meta:
        db_table    = 'calipertypes'


class InteriorGroup(models.Model):
    seat            = models.ForeignKey('Seat',on_delete=models.SET_NULL, null=True)
    dashboard       = models.ForeignKey('Dashboard', on_delete=models.SET_NULL, null=True)
    carpet          = models.ForeignKey('Carpet',on_delete=models.SET_NULL, null=True)
    steering        = models.ForeignKey('Steering', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table    = 'interiorgroups'


class Seat(models.Model):
     model_version_line = models.ForeignKey('ModelVersionLine', on_delete=models.SET_NULL, null=True)
     seat_type          = models.ForeignKey('SeatType', on_delete=models.SET_NULL, null=True)
     code               = models.CharField(max_length=100)

     class Meta:
         db_table       = 'seats'


class SeatType(models.Model):
    color               = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    thumnail_url        = models.URLField(max_length=2000)

    class Meta:
        db_table        = 'seattypes'


class Dashboard(models.Model):
    seat            = models.ForeignKey('Seat',on_delete=models.SET_NULL, null=True)
    dashboard_type  = models.ForeignKey('DashboardType', on_delete=models.SET_NULL, null=True)
    code1           = models.CharField(max_length=100)
    code2           = models.CharField(max_length=100)

    class Meta:
        db_table    = 'dashboards'


class DashboardType(models.Model):
    color           = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    thumnail_url    = models.URLField(max_length=2000)

    class Meta:
        db_table    = 'dashboardtypes'



class Carpet(models.Model):
    dashboard       = models.ForeignKey('Dashboard', on_delete=models.SET_NULL, null=True)
    carpet_type     = models.ForeignKey('CarpetType', on_delete=models.SET_NULL, null=True)
    code            = models.CharField(max_length=100)

    class Meta:
        db_table    = 'carpets'

class CarpetType(models.Model):
    color           = models.ForeignKey('Color',on_delete=models.SET_NULL, null=True)
    thumnail_url    = models.URLField(max_length=2000)

    class Meta:
        db_table    = 'carpettypes'



class Steering(models.Model):
    dashboard       = models.ForeignKey('Dashboard', on_delete=models.SET_NULL, null=True)
    steering_type   = models.ForeignKey('SteeringType', on_delete=models.SET_NULL, null=True)
    code            = models.CharField(max_length=100)

    class Meta:
        db_table   = 'steerings'


class SteeringType(models.Model):
    color           = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    thumnail_url    = models.URLField(max_length=2000)














