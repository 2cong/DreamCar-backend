from django.db import models

class Model(models.Model):
    model               = models.CharField(max_length = 50)

    class Meta:
        db_table        = 'models'


class Version(models.Model):
    version             = models.CharField(max_length = 50)
    
    class Meta:
        db_table        = 'versions'


class Line(models.Model):
    line                = models.CharField(max_length = 50)

    class Meta:
        db_table        = 'lines'


class Spec(models.Model):
    acceleration        = models.DecimalField(max_digits = 10, decimal_places = 2)
    max_speed           = models.IntegerField(default = 0)
    displacement        = models.IntegerField(default = 0)
    max_torque          = models.IntegerField(default = 0)
    max_power           = models.IntegerField(default = 0)
    engine_layout       = models.CharField(max_length = 50)
    engine_stroke       = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    class Meta:
        db_table        = 'specs'

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
