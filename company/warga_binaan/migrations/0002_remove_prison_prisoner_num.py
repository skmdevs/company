# Generated by Django 3.1.7 on 2021-03-04 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warga_binaan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prison',
            name='prisoner_num',
        ),
    ]
