from django import forms
from django.forms import ModelForm
from Crud.models import Buses

class BusesForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Buses
        fields = '__all__'
        widgets = {
            'año_fabricado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'año_modelo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }