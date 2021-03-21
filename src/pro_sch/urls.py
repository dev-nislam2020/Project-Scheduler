from django.urls import path

from pro_sch.views import (FeatureCreateView, FrameworkCreateView,
                           FrameworkUpdateView, InterfaceCreateView,
                           LanguageCreateView, LanguageUpdateView,
                           LogicalCreateView, ProjectCreateView,
                           StatusUpdateView)

urlpatterns = [
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),

    path('language/create/', LanguageCreateView.as_view(), name='language-create'),
    path('language/<int:pk>/update/', LanguageUpdateView.as_view(), name='language-update'),

    path('framework/create/', FrameworkCreateView.as_view(), name='framework-create'),
    path('framework/<int:pk>/update/', FrameworkUpdateView.as_view(), name='framework-update'),

    path('backend/create/', LogicalCreateView.as_view(), name='backend-create'),
    path('frontend/create/', InterfaceCreateView.as_view(), name='interface-create'),
    path('feature/create/', FeatureCreateView.as_view(), name='feature-create'),

    path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
]
