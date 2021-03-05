# Generated by Django 3.1.7 on 2021-03-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prisoner_num', models.CharField(max_length=15)),
                ('no_reg', models.CharField(max_length=25)),
                ('nama', models.CharField(max_length=100)),
                ('pasal', models.CharField(max_length=25)),
                ('hukuman', models.CharField(max_length=25)),
                ('prisoner_status', models.CharField(max_length=25)),
            ],
        ),
    ]