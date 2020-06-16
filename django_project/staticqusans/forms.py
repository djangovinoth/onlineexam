from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from ckeditor.widgets import CKEditorWidget

from .models import StaticQuestions

#     updateddate = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'candiateemailid','class': "form-control",'placeholder': 'candiateemailid'}))


class StaticQuestionsForm(forms.Form):
    TEHCNOLOGY= [
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('MANUALTESTING', 'MANUALTESTING'),
        ('SELENIUM', 'SELENIUM'),
        ]

    technology = forms.ChoiceField(choices=TEHCNOLOGY,widget=forms.Select(attrs={'name':'technology','class':'form-control'}))
    question=forms.CharField(widget=CKEditorWidget(attrs={'label':'question','name':'question','class': "form-control"}))
    answer = forms.CharField(widget=CKEditorWidget(attrs={'name':'answer','class': "form-control"}))
