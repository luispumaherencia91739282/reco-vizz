# Generated by Django 4.1.2 on 2022-10-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_remove_persona_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=0, verbose_name='Edad'),
        ),
    ]
