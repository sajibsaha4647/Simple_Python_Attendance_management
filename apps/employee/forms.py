from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'salary']

    def clean_name(self):
        name = " ".join(self.cleaned_data['name'].split())
        if not name:
            raise forms.ValidationError("Employee name is required")
        return name

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        duplicates = Employee.objects.filter(email__iexact=email)
        if self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise forms.ValidationError("An employee with this email already exists")
        return email
