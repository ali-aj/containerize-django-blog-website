# Generated by Django 4.2.2 on 2023-08-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_blogdata_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='image1',
            field=models.ImageField(default='', upload_to='home/images/'),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='image2',
            field=models.ImageField(null=True, upload_to='home/images/'),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='image3',
            field=models.ImageField(null=True, upload_to='home/images/'),
        ),
    ]
