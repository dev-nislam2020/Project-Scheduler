from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from pro_sch.forms import ProjectForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "pro_sch/home.html"

class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = "pro_sch/create.html"
