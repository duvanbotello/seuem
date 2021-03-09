# Generated by Django 3.1.7 on 2021-03-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210307_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadosModulo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo Estudiantil')),
                ('resultado_liderazgo', models.CharField(max_length=10, null=True, verbose_name='Resultado liderazgo')),
                ('resultado_trabajo_equipo', models.CharField(max_length=10, null=True, verbose_name='Resultado trabajo en equipo')),
                ('resultado_resilencia', models.CharField(max_length=10, null=True, verbose_name='Resultado resilencia')),
                ('resultado_inovacion', models.CharField(max_length=10, null=True, verbose_name='Resultado inovacion')),
                ('resultado_creatividad', models.CharField(max_length=10, null=True, verbose_name='Resultado creatividad')),
                ('resultado_total', models.CharField(max_length=10, null=True, verbose_name='Resultado Total')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.estudiantes')),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
            },
        ),
    ]