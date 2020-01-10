# Generated by Django 2.2.7 on 2020-01-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossacmain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='detail',
            field=models.CharField(default='Sin detalle', max_length=500),
        ),
        migrations.AddField(
            model_name='installation',
            name='status',
            field=models.CharField(choices=[('good', 'En buen estado'), ('medium', 'Algo está ocurriendo'), ('bad', 'Defectuoso')], default='good', max_length=100),
        ),
    ]