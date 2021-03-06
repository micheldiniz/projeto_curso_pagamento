# Generated by Django 3.0.8 on 2020-11-13 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_pagamento', '0004_curso_situacao_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos_pagamento.Curso'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='relatorio',
            field=models.FileField(upload_to='relatorio/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividade_usuario_participante', to='cursos_pagamento.Usuario'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='participante',
            field=models.ManyToManyField(related_name='usuario_participante', through='cursos_pagamento.Atividade', to='cursos_pagamento.Usuario'),
        ),
    ]
