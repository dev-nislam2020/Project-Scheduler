from django.urls import path

from pro_sch.views import (FrameworkCreateView, LanguageCreateView,
                           LogicalCreateView, ProjectCreateView)

urlpatterns = [
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('language/create/', LanguageCreateView.as_view(), name='language-create'),
    path('framework/create/', FrameworkCreateView.as_view(), name='framework-create'),
    path('backend/create/', LogicalCreateView.as_view(), name='backend-create'),
]
