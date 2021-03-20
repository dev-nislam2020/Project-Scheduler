from django import forms

from pro_sch.models import Project


# Create your forms here.
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'app_type', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
