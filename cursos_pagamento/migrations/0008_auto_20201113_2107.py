# Generated by Django 3.0.8 on 2020-11-14 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0007_auto_20201113_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos_pagamento.Usuario'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='participante',
            field=models.ManyToManyField(through='cursos_pagamento.Atividade', to='cursos_pagamento.Usuario'),
        ),
    ]