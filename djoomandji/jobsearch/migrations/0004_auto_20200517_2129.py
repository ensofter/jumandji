# Generated by Django 3.0.6 on 2020-05-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0003_auto_20200517_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_images'),
        ),
    ]
