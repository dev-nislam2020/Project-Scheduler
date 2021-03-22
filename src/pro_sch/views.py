from django.shortcuts import get_object_or_404, reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from pro_sch.forms import (FeatureForm, FrameworkForm, InterfaceForm,
                           LanguageForm, LogicalForm, ProjectForm, StatusForm)
from pro_sch.models import Framework, Language, Project, Status


# Create your views here.
class HomeView(TemplateView):
    template_name = "pro_sch/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Project"
        return context

class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Project"
        return context
    
    def get_success_url(self):
        project = Project.objects.order_by('-pk')[0]
        return reverse('backend-create', kwargs={'pk': project.pk}) 

class LanguageCreateView(CreateView):
    form_class = LanguageForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LanguageCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Language"
        context['is_language'] = True
        return context

class LanguageListView(ListView):
    queryset = Language.objects.all()
    template_name = "pro_sch/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LanguageListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Language List"
        context['name'] = "Language"
        context['is_language'] = True
        return context


class LanguageUpdateView(UpdateView):
    form_class = LanguageForm
    queryset = Language.objects.all()
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LanguageUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Language Update"
        return context
    
    def get_success_url(self):
        return reverse('language-list')

class FrameworkCreateView(CreateView):
    form_class = FrameworkForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FrameworkCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Framework"
        context['is_framework'] = True
        return context

class FrameworkListView(ListView):
    queryset = Framework.objects.all()
    template_name = "pro_sch/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FrameworkListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Framework List"
        context['name'] = "Framework"
        context['is_framework'] = True
        return context

class FrameworkUpdateView(UpdateView):
    form_class = FrameworkForm
    queryset = Framework.objects.all()
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FrameworkUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Framework Update"
        return context

    def get_success_url(self):
        return reverse('framework-list')

class LogicalCreateView(CreateView):
    form_class = LogicalForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LogicalCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Backend"
        return context
    
    def form_valid(self, form):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        form.instance.project = self.project
        return super(LogicalCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('frontend-create', kwargs={'pk': self.kwargs['pk']})

class InterfaceCreateView(CreateView):
    form_class = InterfaceForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InterfaceCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Frontend"
        return context

    def form_valid(self, form):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        form.instance.project = self.project
        return super(InterfaceCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('home')

class FeatureCreateView(CreateView):
    form_class = FeatureForm
    template_name = "pro_sch/create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FeatureCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_name'] = "Add Project Feature"
        return context
    
    def form_valid(self, form):
        self.project = get_object_or_404(Project, id=self.kwargs['pk'])
        form.instance.project = self.project
        return super(FeatureCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('home')


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
