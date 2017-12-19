# Generated by Django 2.0 on 2017-12-19 21:40

from datetime import date

from django.db import migrations


def create_initial_developers(apps, schema_editor):
    Developer = apps.get_model('developers', 'Developer')
    University = apps.get_model('developers', 'University')
    Education = apps.get_model('developers', 'Education')
    Company = apps.get_model('developers', 'Company')
    Employment = apps.get_model('developers', 'Employment')
    Skill = apps.get_model('developers', 'Skill')

    # Alexander Chistyakov
    achistyakov = Developer.objects.create(name='Alexander', surname='Chistyakov')
    python_skill = Skill.objects.create(name='Python')
    achistyakov.skills.add(python_skill)
    achistyakov.skills.create(name='Docker')
    achistyakov.skills.create(name='SQL')
    achistyakov.skills.create(name='RabbitMQ')
    achistyakov.skills.create(name='Redis')
    achistyakov.skills.create(name='Celery')
    achistyakov.skills.create(name='Sentry')
    achistyakov.skills.create(name='git')

    itmo = University.objects.create(name='ITMO University')
    Education.objects.create(
        developer=achistyakov,
        university=itmo,
        year_of_graduation=2013,
    )

    fsecure = Company.objects.create(name='F-Secure Inc.')
    Employment.objects.create(
        developer=achistyakov,
        company=fsecure,
        role='Junior Test Engineer',
        start_date=date(year=2012, month=4, day=1),
        end_date=date(year=2012, month=11, day=1),
    )
    Employment.objects.create(
        developer=achistyakov,
        company=fsecure,
        role='Test Engineer',
        start_date=date(year=2013, month=10, day=1),
        end_date=date(year=2015, month=7, day=1),
    )
    vispamedia = Company.objects.create(name='VispaMedia')
    Employment.objects.create(
        developer=achistyakov,
        company=vispamedia,
        role='Test Automation Engineer',
        start_date=date(year=2016, month=6, day=1),
        end_date=date(year=2017, month=12, day=8),
    )

    # Yana Burova
    yburova = Developer.objects.create(name='Yana', surname='Burova')
    yburova.skills.create(name='Soft skill')
    yburova.skills.add(python_skill)

    saprun = Company.objects.create(name='Saprun')
    Employment.objects.create(
        developer=yburova,
        company=saprun,
        role='HR Manager',
        start_date=date(year=2010, month=1, day=1),
        end_date=None
    )

    # Dmitry Bugrov
    dbugrov = Developer.objects.create(name='Dmitry', surname='Bugrov')
    assert not dbugrov.skills.all()  # no skills
    Employment.objects.create(
        developer=dbugrov,
        company=saprun,
        role='Project Manager',
        start_date=date(year=2010, month=1, day=1),
        end_date=None
    )


class Migration(migrations.Migration):
    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_developers),
    ]