# Generated by Django 3.0.8 on 2020-11-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0009_auto_20201113_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='complementacao',
            field=models.CharField(max_length=100, null=True, verbose_name='Complementação'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='atividade',
            name='validation_date',
            field=models.DateField(editable=False, null=True),
        ),
    ]
