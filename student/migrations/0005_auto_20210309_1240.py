# Generated by Django 3.1.7 on 2021-03-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_resultadosmodulo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadosmodulo1',
            name='codigo_estudiante',
            field=models.CharField(max_length=100, null=True, verbose_name='Codigo Estudiantil'),
        ),
    ]
