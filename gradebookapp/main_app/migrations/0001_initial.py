# Generated by Django 4.1.7 on 2023-03-14 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('category', models.TextField(max_length=100)),
                ('weight', models.IntegerField()),
                ('duedate', models.DateField(verbose_name='due date')),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('assignments', models.ManyToManyField(through='main_app.Grade', to='main_app.assignment')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cohort'),
        ),
    ]