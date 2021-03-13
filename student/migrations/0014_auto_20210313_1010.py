# Generated by Django 3.1.7 on 2021-03-13 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20210313_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='docente',
            field=models.ForeignKey(default=None, help_text='Seleccione un docente y asignelo', on_delete=django.db.models.deletion.CASCADE, related_name='Docente', to='student.docentes', verbose_name='Asigne un docente'),
        ),
    ]
