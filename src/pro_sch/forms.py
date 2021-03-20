from django import forms

from pro_sch.models import (Feature, Framework, Interface, Language, Logical,
                            Project)


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

class LogicalForm(forms.ModelForm):
    class Meta:
        model = Logical
        fields = ['language', 'framework', 'db_name']

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['language', 'framework']

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'oparetion', 'notes']
