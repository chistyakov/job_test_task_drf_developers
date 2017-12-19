# Generated by Django 2.0 on 2017-12-19 19:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_graduation', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)])),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.Company')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.University'),
        ),
        migrations.AddField(
            model_name='developer',
            name='educations',
            field=models.ManyToManyField(blank=True, related_name='graduated', through='developers.Education', to='developers.University'),
        ),
        migrations.AddField(
            model_name='developer',
            name='employment_history',
            field=models.ManyToManyField(blank=True, related_name='employees_history', through='developers.Employment', to='developers.Company'),
        ),
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='developers', to='developers.Skill'),
        ),
    ]
