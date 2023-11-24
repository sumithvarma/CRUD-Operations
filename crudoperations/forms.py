from django import forms
from crudoperations.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email','salary','address']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'contact': forms.TextInput(attrs={'class': 'form-control'}),
                   'salary': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   }
