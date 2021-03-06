# Generated by Django 2.2.5 on 2019-09-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField()),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('mq135', models.FloatField()),
                ('mq2', models.FloatField()),
                ('mq4', models.FloatField()),
                ('dust', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
