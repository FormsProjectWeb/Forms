from django import forms
from Answering.models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question',)
