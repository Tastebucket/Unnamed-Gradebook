# Generated by Django 4.1.7 on 2023-03-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(to='main_app.cohort'),
        ),
    ]
