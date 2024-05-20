from django import forms
from django.contrib.auth.models import User
from .models import Producto, CategoriaProducto, Especialidad


class RegistroForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=100)
    email = forms.EmailField(label='Correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirmar_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden."
            )

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_especialidad', 'id_categoria', 'codigo_upc', 'nombre', 'marca']

# forms.py
class ModificarForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_especialidad', 'id_categoria', 'codigo_upc', 'nombre', 'marca']

    def __init__(self, *args, **kwargs):
        super(ModificarForm, self).__init__(*args, **kwargs)
        # Agregar opciones para seleccionar el nombre, marca y código UPC de productos existentes
        self.fields['nombre'].queryset = Producto.objects.all()
        self.fields['marca'].queryset = Producto.objects.all()
        self.fields['codigo_upc'].queryset = Producto.objects.all()


class EliminarProForm(forms.Form):
    confirmacion = forms.BooleanField(label="Confirmar eliminación")
    nombre_producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),  # Consulta para obtener todos los productos
        label="Nombre del Producto",
        empty_label=None,  # Eliminar la opción vacía
    )