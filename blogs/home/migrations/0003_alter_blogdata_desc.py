# Generated by Django 4.2.2 on 2023-08-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blogdata_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='desc',
            field=models.TextField(max_length=10000),
        ),
    ]
