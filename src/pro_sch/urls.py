from django.urls import path

from pro_sch.views import (FeatureCreateView, FrameworkCreateView,
                           FrameworkListView, FrameworkUpdateView,
                           InterfaceCreateView, LanguageCreateView,
                           LanguageListView, LanguageUpdateView,
                           LogicalCreateView, ProjectCreateView,
                           StatusUpdateView)

urlpatterns = [
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),

    path('language/create/', LanguageCreateView.as_view(), name='language-create'),
    path('language/list/', LanguageListView.as_view(), name='language-list'),
    path('language/<int:pk>/update/', LanguageUpdateView.as_view(), name='language-update'),

    path('framework/create/', FrameworkCreateView.as_view(), name='framework-create'),
    path('framework/list/', FrameworkListView.as_view(), name='framework-list'),
    path('framework/<int:pk>/update/', FrameworkUpdateView.as_view(), name='framework-update'),

    path('backend/<int:pk>/create/', LogicalCreateView.as_view(), name='backend-create'),
    path('frontend/<int:pk>/create/', InterfaceCreateView.as_view(), name='frontend-create'),

    path('feature/create/', FeatureCreateView.as_view(), name='feature-create'),

    path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
]
