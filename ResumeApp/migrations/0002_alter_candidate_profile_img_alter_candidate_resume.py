# Generated by Django 4.1.2 on 2022-10-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.FileField(blank=True, upload_to='resume'),
        ),
    ]
