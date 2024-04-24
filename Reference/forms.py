from django import forms
from Reference.models import Reference

class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ('subject', 'topics')
