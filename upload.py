import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from car.models import *

# model
CSV_PATH = './CSV/model.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Model.objects.create(
            name = row['model']
        )

# version
CSV_PATH = './CSV/version.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Version.objects.create(
             name = row['version']
         )

# line
CSV_PATH = './CSV/line.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Line.objects.create(
            name = row['line']
        )

# spec
CSV_PATH = './CSV/spec.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Spec.objects.create(
            acceleration = row['acceleration'],
            max_speed = row['max_speed'],
            displacement = row['displacement'],
            max_torque = row['max_torque'],
            max_power = row['max_power'],
            engine_layout = row['engine_layout'],
            engine_bore = row['engine_bore'],
            engine_stroke = row['engine_stroke']
        )

# dimension
CSV_PATH = './CSV/dimension.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Dimension.objects.create(
            length = row['length'],
            width_side = row['width_side'],
            width_noside = row['width_noside'],
            height = row['height'],
            wheelbase = row['wheelbase'],
            front_track = row['front_track'],
            rear_track = row['rear_track'],
            front_overhang = row['front_overhang'],
            rear_overhang = row['rear_overhang'],
            turning_circle = row['turning_circle'],
            boot_capacity = row['boot_capacity'],
            fuel_tank_capacity = row['fuel_tank_capacity'],
            unladen_weight = row['unladen_weight'],
            kerb_weight = row['kerb_weight'],
            tire_size_front = row['tire_size_front'],
            tire_size_back = row['tire_size_back']
        )

# modelversionline
CSV_PATH = './CSV/modelversionline.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        ModelVersionLine.objects.create(
            model = Model.objects.get(id=row['model_id']),
            version = Version.objects.get(id=row['version_id']),
            line = Line.objects.get(id=row['line_id']),
            spec = Spec.objects.get(id=row['spec_id']),
            dimension = Dimension.objects.get(id=row['dimension_id'])
        )

# color
CSV_PATH = './CSV/color.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Color.objects.create(
            name = row['color_name']
        )

# color_type
CSV_PATH = './CSV/color_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        ColorType.objects.create(
            type_name = row['type']
        )

# Seat_type
CSV_PATH = './CSV/seat_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        SeatType.objects.create(
            color = Color.objects.get(id=row['color_id']),
            thumbnail_url = row['thumbnail_url']
        )

# seat
CSV_PATH = './CSV/seat.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Seat.objects.create(
            model_version_line = ModelVersionLine.objects.get(id=row['model_version_line_id']),
            seat_type = SeatType.objects.get(id=row['seat_type_id']),
            code = row['car_seat_image_code']
        )

# dashboard_type
CSV_PATH = './CSV/dashboard_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        DashboardType.objects.create(
            color = Color.objects.get(id=row['color_id']),
            thumbnail_url = row['thumbnail_url']
        )

# dashboard
CSV_PATH = './CSV/dashboard.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Dashboard.objects.create(
            seat = Seat.objects.get(id=row['seat_id']),
            dashboard_type = DashboardType.objects.get(id=row['dashboard_type_id']),
            code1 = row['car_dashboard_image_code'],
            code2 = row['code2']
        )

# carpet_type
CSV_PATH = './CSV/carpet_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        CarpetType.objects.create(
            color = Color.objects.get(id=row['color_id']),
            thumbnail_url = row['thumbnail_url']
        )

# carpet
CSV_PATH = './CSV/carpet.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Carpet.objects.create(
            dashboard = Dashboard.objects.get(id=row['dashboard_id']),
            carpet_type = CarpetType.objects.get(id=row['carpet_type_id']),
            code = row['car_carpet_image_code']
        )

# steering_type
CSV_PATH = './CSV/steering_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        SteeringType.objects.create(
            color = Color.objects.get(id=row['color_id']),
            thumbnail_url = row['thumbnail_url']
        )

# steering
CSV_PATH = './CSV/steering.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Steering.objects.create(
            dashboard = Dashboard.objects.get(id=row['dashboard_id']),
            steering_type = SteeringType.objects.get(id=row['steering_type_id']),
            code = row['car_steering_image_code']
        )

# interior_group
CSV_PATH = './CSV/interior_group.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        InteriorGroup.objects.create(
            seat = Seat.objects.get(id=row['seat_id']),
            dashboard = Dashboard.objects.get(id=row['dashboard_id']),
            carpet = Carpet.objects.get(id=row['carpet_id']),
            steering = Steering.objects.get(id=row['steering_id'])
        )

# package
CSV_PATH = './CSV/package.csv'

with open(CSV_PATH,newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Package.objects.create(
            name = row['name'],
            description = row['description'],
            description_list = row['desc_list']
        )

# exterior_type
CSV_PATH = './CSV/exterior_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        ExteriorType.objects.create(
            color         = Color.objects.get(id = row['color_id']),
            color_type    = ColorType.objects.get(id= row['color_type_id']),
            thumbnail_url = row['thumbnail_url']
         )

# exterior
CSV_PATH = './CSV/exterior.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Exterior.objects.create(
            model_version_line  = ModelVersionLine.objects.get(id = row['model_version_line_id']),
            exterior_type       = ExteriorType.objects.get(id = row['exterior_type_id']),
            code                = row['car_exterior_image_code']
         )

# wheel_type
CSV_PATH = './CSV/wheel_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        WheelType.objects.create(
            name           = row['wheel_name'],
            thumbnail_url  = row['thumbnail_url'],
         )

# wheel
CSV_PATH = './CSV/wheel.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Wheel.objects.create(
            model_version_line      = ModelVersionLine.objects.get(id = row['model_version_line_id']),
            wheel_type              = WheelType.objects.get(id = row['wheel_type_id']),
            code                    = row['car_wheel_code'],
         )

# caliper type
CSV_PATH = './CSV/caliper_type.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile) #dictreader , reaader

    for row in data_reader:
        CaliperType.objects.create(
             color           = Color.objects.get(id = row['color_id']),
             thumbnail_url   = row['thumbnail_url']
         )

# caliper
CSV_PATH = './CSV/caliper.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile) #dictreader , reaader

    for row in data_reader:
        Caliper.objects.create(
             model_version_line  = ModelVersionLine.objects.get(id = row['model_version_line_id']),
             caliper_type        = CaliperType.objects.get(id = row['caliper_type_id']),
             code                = row['code']
         )

# exterior_group
CSV_PATH = './CSV/exterior_group.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile) #dictreader , reaader

    for row in data_reader:
        ExteriorGroup.objects.create(
             exterior         = Exterior.objects.get(id = row['exterior_id']),
             wheel            = Wheel.objects.get(id = row['wheel_id']),
             caliper          = Caliper.objects.get(id = row['caliper_id'])
        )
