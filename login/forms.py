from django import forms

from student.models import Estudiantes, Grade


class FormularioRegistrar(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Contraseña',
            'id': 'pass1',
            'required': 'required',
        }
    ), label='')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmar contraseña',
            'id': 'pass1',
            'required': 'required',
        }
    ), label='')

    class Meta:
        model = Estudiantes
        fields = (
            'nombres', 'apellidos', 'codigo_estudiante', 'grado', 'edad', 'nombre_acudiente', 'telefono_contacto',
            'correo')
        labels = {
            'nombres': '', 'apellidos': '', 'codigo_estudiante': '', 'grado': '', 'edad': '', 'nombre_acudiente': '',
            'telefono_contacto': '', 'correo': ''
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Nombres',
                    'required': 'required',
                    'autocomplete': 'off',
                }
            ), 'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Apellidos',
                    'required': 'required',
                    'autocomplete': 'off'
                }
            ), 'codigo_estudiante': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Codigo de estudiante',
                    'required': 'required',
                    'autocomplete': 'off',
                    'type': 'number'
                }
            ), 'grado': forms.Select(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Grado',
                    'required': 'required',
                    'autocomplete': 'off',
                }
            ), 'edad': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Edad',
                    'required': 'required',
                    'autocomplete': 'off',
                    'type': 'number'
                }
            ), 'nombre_acudiente': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Nombre Acudiente',
                    'required': 'required',
                    'autocomplete': 'off'
                }
            ), 'telefono_contacto': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Telefono de contacto',
                    'required': 'required',
                    'autocomplete': 'off',
                    'type': 'number'
                }
            ), 'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Correo Electronico',
                    'required': 'required',
                    'autocomplete': 'off',
                }
            ),
        }

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password1 != password2:
                raise forms.ValidationError('Por favor, verificar que las contraseñas sean iguales')
            else:
                return password2
