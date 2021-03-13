# Generated by Django 3.1.7 on 2021-03-11 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210311_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregaarchivos',
            name='codigo_estudiante',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo Estudiantil'),
        ),
        migrations.AlterField(
            model_name='entregaarchivos',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.estudiantes', unique=True),
        ),
    ]
