# Generated by Django 4.2.1 on 2023-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelthCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('madicine', models.CharField(max_length=30)),
                ('timing', models.TimeField()),
            ],
        ),
    ]
