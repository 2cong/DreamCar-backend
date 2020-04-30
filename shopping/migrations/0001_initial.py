# Generated by Django 3.0.5 on 2020-04-30 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'address_cities',
            },
        ),
        migrations.CreateModel(
            name='ExpectDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'expect_dates',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='StoreInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=50)),
                ('service_center', models.BooleanField()),
                ('exhibition_center', models.BooleanField()),
                ('telephone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('description1', models.CharField(max_length=2000)),
                ('description2', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'store_informations',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('phonenumber', models.CharField(max_length=200)),
                ('address_detail', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=200)),
                ('address_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.AddressCity')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.Gender')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='TestDriveSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us', models.TextField()),
                ('expect_date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.ExpectDate')),
                ('model_version_line', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.ModelVersionLine')),
                ('store_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.StoreInformation')),
            ],
            options={
                'db_table': 'test_drive_schedules',
            },
        ),
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_car_model', models.CharField(max_length=50)),
                ('test_drive_schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.TestDriveSchedule')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.User')),
            ],
            options={
                'db_table': 'test_drives',
            },
        ),
    ]
