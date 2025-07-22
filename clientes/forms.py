from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'mensaje': 'Mensaje',
        }
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }
