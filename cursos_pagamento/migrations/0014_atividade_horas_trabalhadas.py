# Generated by Django 3.0.8 on 2020-11-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0013_remove_atividade_horas_trabalhadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='horas_trabalhadas',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
