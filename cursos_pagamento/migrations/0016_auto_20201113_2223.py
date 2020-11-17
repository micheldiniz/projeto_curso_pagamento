# Generated by Django 3.0.8 on 2020-11-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0015_auto_20201113_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='valor_pago_servidor',
            field=models.CharField(editable=False, max_length=100, null=True, verbose_name='Valor pago para o servidor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='valor_total_curso',
            field=models.CharField(editable=False, max_length=100, null=True, verbose_name='Valor total pago pelo curso'),
        ),
    ]