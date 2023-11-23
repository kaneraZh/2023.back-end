# Generated by Django 4.2.7 on 2023-11-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now_add=True)),
                ('tiempo_ejecucion', models.DurationField()),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
    ]
