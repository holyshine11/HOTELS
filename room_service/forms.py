from django import forms
from .models import LangChoice

class LangChoiceForm(forms.ModelForm):
    class Meta:
        model = LangChoice
        fields = ['language', 'room_number']
