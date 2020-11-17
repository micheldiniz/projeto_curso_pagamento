# Generated by Django 3.0.8 on 2020-11-17 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0016_auto_20201113_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='carga_horaria',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='participante',
            field=models.ManyToManyField(null=True, through='cursos_pagamento.Atividade', to='cursos_pagamento.Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_chefe',
            field=models.BooleanField(default=False, verbose_name='Chefe de setor?'),
        ),
    ]