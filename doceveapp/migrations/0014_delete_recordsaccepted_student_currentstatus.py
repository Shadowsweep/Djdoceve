# Generated by Django 4.1.6 on 2023-07-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doceveapp', '0013_recordsaccepted'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecordsAccepted',
        ),
        migrations.AddField(
            model_name='student',
            name='currentstatus',
            field=models.CharField(default='', max_length=70),
        ),
    ]