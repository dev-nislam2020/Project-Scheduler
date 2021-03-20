from django.urls import path

from pro_sch.views import ProjectCreateView

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='project-create'),
]
