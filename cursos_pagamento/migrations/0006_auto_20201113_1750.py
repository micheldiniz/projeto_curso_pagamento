# Generated by Django 3.1.3 on 2020-11-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0005_auto_20201113_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='complementacao',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='atividade',
            name='validation_date',
            field=models.DateField(editable=False, null=True),
        ),
    ]