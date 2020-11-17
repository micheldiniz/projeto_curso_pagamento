# Generated by Django 3.0.8 on 2020-11-12 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=10)),
                ('login', models.CharField(max_length=15)),
                ('is_chefe', models.BooleanField(default=False)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos_pagamento.Setor')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagamento', models.CharField(max_length=10)),
                ('curso', models.ManyToManyField(to='cursos_pagamento.Curso')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_participante', to='cursos_pagamento.Usuario'),
        ),
        migrations.AddField(
            model_name='curso',
            name='responsavel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_responsavel', to='cursos_pagamento.Usuario'),
        ),
    ]