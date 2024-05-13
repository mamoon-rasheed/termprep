from django import forms

from crudoperations.models import Student


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("__all__")
