from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "pro_sch/home.html"
