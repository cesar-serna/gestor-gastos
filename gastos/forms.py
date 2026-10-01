from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ["concepto", "monto", "fecha"]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }