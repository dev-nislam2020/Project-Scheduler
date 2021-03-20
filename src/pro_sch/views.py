from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from pro_sch.forms import LanguageForm, ProjectForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "pro_sch/home.html"

class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Project"
        return context

class LanguageCreateView(CreateView):
    form_class = LanguageForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LanguageCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Language"
        return context


