from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from ckeditor.widgets import CKEditorWidget

from .models import Questions

#     updateddate = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'candiateemailid','class': "form-control",'placeholder': 'candiateemailid'}))


class QuestionsForm(forms.Form):
    TEHCNOLOGY= [
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('MANUALTESTING', 'MANUALTESTING'),
        ('SELENIUM', 'SELENIUM'),
        ]
    LEVEL= [
        ('LEVEL1', 'LEVEL1'),
        ('LEVEL2', 'LEVEL2'),
        ('LEVEL3', 'LEVEL3'),
        ('LEVEL4', 'LEVEL4'),
        ('LEVEL5', 'LEVEL5'),
        ('LEVEL6', 'LEVEL6'),
        ('LEVEL7', 'LEVEL7'),
        ]
    ANSWER= [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),

        ]

    level = forms.ChoiceField(choices=LEVEL,widget=forms.Select(attrs={'name':'level','class':'form-control'}))
    technology = forms.ChoiceField(choices=TEHCNOLOGY,widget=forms.Select(attrs={'name':'technology','class':'form-control'}))
    # question = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'name':'question','class': "form-control"}))
    question=forms.CharField(widget=CKEditorWidget(attrs={'label':'question','name':'question','class': "form-control"}))

    answera = forms.CharField(widget=CKEditorWidget(attrs={'name':'answera','class': "form-control"}))
    answerb = forms.CharField(widget=CKEditorWidget(attrs={'name':'answerb','class': "form-control"}))
    answerc = forms.CharField(widget=CKEditorWidget(attrs={'name':'answerc','class': "form-control"}))
    answerd = forms.CharField(widget=CKEditorWidget(attrs={'name':'answerd','class': "form-control"}))    
    correctanswer = forms.ChoiceField(label='CORRECT ANSWER',choices=ANSWER,widget=forms.Select(attrs={'name':'correctanswer','class':'form-control'}))
