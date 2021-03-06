# Generated by Django 3.1.7 on 2021-04-17 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activar_convocatoria', models.BooleanField(default=False, verbose_name='Activar/Desactivar')),
                ('proxima_convocatoria', models.DateField(null=True, verbose_name='Apertura de plataforma')),
            ],
            options={
                'verbose_name': 'Convocatoria',
                'verbose_name_plural': 'Convocatorias',
            },
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, null=True, verbose_name='Apellidos')),
                ('documento', models.CharField(max_length=100, null=True, unique=True, verbose_name='Documento identidad')),
                ('edad', models.CharField(max_length=10, null=True, verbose_name='Edad')),
                ('titulo', models.CharField(max_length=100, null=True, verbose_name='Titulo academico')),
                ('telefono_contacto', models.CharField(max_length=100, null=True, verbose_name='Contacto')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
            },
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('nombres', models.CharField(max_length=100, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, null=True, verbose_name='Apellidos')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo Estudiantil')),
                ('edad', models.CharField(max_length=10, null=True, verbose_name='Edad')),
                ('nombre_acudiente', models.CharField(max_length=100, null=True, verbose_name='Nombre del acudiente')),
                ('telefono_contacto', models.CharField(max_length=100, null=True, verbose_name='Contacto')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('docente', models.OneToOneField(blank=True, default=None, help_text='Seleccione un docente y asignelo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Docente', to='student.docentes', verbose_name='Asigne un docente')),
                ('grado', models.ForeignKey(blank=True, help_text='Seleccione un grado y asignelo', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Grado', to='student.grade', verbose_name='Asigne un grado')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='ResultadosModulo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, verbose_name='Codigo Estudiantil')),
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
        migrations.CreateModel(
            name='EntregaArchivosModulo3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo Estudiantil')),
                ('formato_guia', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Plantilla Guia')),
                ('nota', models.CharField(max_length=10, null=True, verbose_name='Ingrese Nota')),
                ('observaciones', models.TextField(null=True, verbose_name='Ingrese Observaciones')),
                ('rubrica', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Rebrica de calificacion')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EntregaArchivos3', to='student.estudiantes')),
            ],
            options={
                'verbose_name': 'Entrega Modulo 3',
                'verbose_name_plural': 'Entregas Modulo 3',
            },
        ),
        migrations.CreateModel(
            name='EntregaArchivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=100, null=True, unique=True, verbose_name='Codigo Estudiantil')),
                ('formato_guia', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Plantilla Guia')),
                ('nota', models.CharField(max_length=10, null=True, verbose_name='Ingrese Nota')),
                ('observaciones', models.TextField(null=True, verbose_name='Ingrese Observaciones')),
                ('rubrica', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Rebrica de calificacion')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.estudiantes')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
            },
        ),
    ]
