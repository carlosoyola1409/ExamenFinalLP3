from django import forms
from django.core import validators

class form_carrera(forms.Form):
    codigo = forms.CharField(
        label="CODIGO:",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Igrese COdigo'}
        )
    )

    nombre = forms.CharField(
        label="NOMBRE:",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Ingrese Codigo'}
        )
    )

    hora = forms.IntegerField(
        label="HORAS:",
        required=True,
        widget=forms.NumberInput(
            attrs={'placeholder':'Ingrese horas'}
            
        )
    )

    creditos = forms.IntegerField(
        label="CREDITOS:",
        required=True,
        widget=forms.NumberInput(
            attrs={'placeholder':'Ingrese Creditos'}
            
        )
    )
    
    opciones_estado = [(1,'si'),(0,'no')]

    estado = forms.TypedChoiceField(
        label="Estado",
        choices=opciones_estado
    ) 

class form_carrera2(forms.Form):
    nombre = forms.CharField(
        label="NOmbre:",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Digite Nombre'}
        )
    )

    nombrecorto = forms.CharField(
        label="NOmbre COrto:",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'NOmbre Corto'}
        )
    )

    opciones_estado = [(1,'si'),(0,'no')]

    estado = forms.TypedChoiceField(
        label="Estdo",
        choices=opciones_estado
    )

