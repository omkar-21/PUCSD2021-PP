# Generated by Django 3.2 on 2021-04-28 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_college_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]