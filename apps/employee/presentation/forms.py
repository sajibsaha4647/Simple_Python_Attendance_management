from django import forms


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=30)
    salary = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0)
