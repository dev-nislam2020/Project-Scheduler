from django import forms

from pro_sch.models import Framework, Language, Project


# Create your forms here.
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'app_type', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']

class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ['name']
