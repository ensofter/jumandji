# Generated by Django 3.0.6 on 2020-05-22 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0005_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.IntegerField(),
        ),
    ]