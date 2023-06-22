# forms.py
from django import forms

class MyForm(forms.Form):
    dropdown_choices = (
        ('All', 'All'),
        ('850', '850'),
        ('810', '810'),
        
    )
    dropdown_field = forms.ChoiceField(choices=dropdown_choices,label='Select ISA type')
