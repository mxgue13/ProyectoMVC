# Generated by Django 3.2.8 on 2023-02-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Tdocumento',
            name='descripcion',
            field=models.CharField(max_length=40),
        ),
    ]
