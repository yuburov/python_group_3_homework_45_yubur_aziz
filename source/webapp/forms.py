from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOISES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=300, required=True, label='Description')
    specific = forms.CharField(max_length=3000, required=False, label='Specification', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOISES, required=False, label='Status')
    date_of_completion = forms.DateField(required=False , label='Date of completion')


