from django import forms
from modelapp.models import Employee
class EmployeeForm(forms.ModelForm):
    name=forms.CharField(max_length=20)
    sno=forms.IntegerField()
    email=forms.EmailField()
    phn=forms.IntegerField()
    addr=forms.CharField(max_length=40)
    com=forms.CharField(max_length=20)
    skills=forms.CharField(max_length=40)
    class Meta:
        model=Employee
        fields="__all__"
