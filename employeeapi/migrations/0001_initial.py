# Generated by Django 3.1.4 on 2020-12-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeId', models.CharField(max_length=4)),
                ('EmployeeName', models.CharField(max_length=1000)),
                ('EmployeeDesignation', models.CharField(max_length=1000)),
                ('EmployeeSalary', models.CharField(max_length=10)),
                ('EmployeeMobile', models.CharField(max_length=12)),
            ],
        ),
    ]
