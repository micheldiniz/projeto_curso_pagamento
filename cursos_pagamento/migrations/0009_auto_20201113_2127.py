# Generated by Django 3.0.8 on 2020-11-14 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0008_auto_20201113_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='complementacao',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='is_validated',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='validation_date',
        ),
    ]
