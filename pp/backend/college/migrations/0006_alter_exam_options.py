# Generated by Django 3.2 on 2021-04-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_alter_exam_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'get_latest_by': 'date'},
        ),
    ]