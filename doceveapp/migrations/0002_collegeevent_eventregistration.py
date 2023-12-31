# Generated by Django 4.1.6 on 2023-07-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doceveapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(default='', max_length=150)),
                ('startdate', models.CharField(default='', max_length=70)),
                ('enddate', models.CharField(default='', max_length=70)),
                ('starttime', models.CharField(default='', max_length=70)),
                ('endtime', models.CharField(default='', max_length=70)),
                ('eventlocation', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=150)),
                ('facultycoordinatorid', models.CharField(default='', max_length=70)),
                ('studentcoordinatorid1', models.CharField(default='', max_length=70)),
                ('studentcoordinatorid2', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('eid', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('enrollmentid', models.CharField(default='', max_length=70)),
                ('regdate', models.CharField(default='', max_length=70)),
                ('regtime', models.CharField(default='', max_length=70)),
                ('remarks', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
