from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from pro_sch.forms import (FeatureForm, FrameworkForm, InterfaceForm,
                           LanguageForm, LogicalForm, ProjectForm, StatusForm)
from pro_sch.models import Status


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

class FrameworkCreateView(CreateView):
    form_class = FrameworkForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FrameworkCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Framework"
        return context

class LogicalCreateView(CreateView):
    form_class = LogicalForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LogicalCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Backend"
        return context

class InterfaceCreateView(CreateView):
    form_class = InterfaceForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InterfaceCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Frontend"
        return context

class FeatureCreateView(CreateView):
    form_class = FeatureForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FeatureCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Project Feature"
        return context


class StatusUpdateView(UpdateView):
    form_class = StatusForm
    queryset = Status.objects.all()
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(StatusUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Project Status Update"
        return context
