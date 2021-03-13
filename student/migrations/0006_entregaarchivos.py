# Generated by Django 3.1.7 on 2021-03-11 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210309_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregaArchivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, verbose_name='Codigo Estudiantil')),
                ('formato_guia', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Plantilla Guia')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.estudiantes')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
            },
        ),
    ]
