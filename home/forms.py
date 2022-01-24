from django.core import validators
from django import forms
from .models import StudentInfo, StudentAcadmics

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['Roll','Name','Clas','School','Mobile','Address']

class Student(forms.ModelForm):
    class Meta:
        model = StudentAcadmics
        fields = ['Roll_no','Maths','Physics','Chemistry','Biology','English']


widgets = {
         'Roll':forms.TextInput(attrs={'class':'form-control'}),
         'Name': forms.TextInput(attrs={'class':'form-control'}),
         'Clas':forms.TextInput(attrs={'class':'form-control'}),
        'School':forms.TextInput(attrs={'class':'form-control'}),
'Mobile':forms.TextInput(attrs={'class':'form-control'}),
         'Address':forms.TextInput(attrs={'class':'form-control'})
         ,

     }