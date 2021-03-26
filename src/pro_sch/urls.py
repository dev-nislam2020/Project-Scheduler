from django.urls import path

from pro_sch.views import (FeatureCreateView, FeatureListView,
                           FeatureUpdateView, FrameworkCreateView,
                           FrameworkListView, FrameworkUpdateView,
                           InterfaceCreateView, InterfaceUpdateView,
                           LanguageCreateView, LanguageListView,
                           LanguageUpdateView, LogicalCreateView,
                           LogicalUpdateView, ProjectCreateView,
                           ProjectDeleteView, ProjectDetailView,
                           ProjectUpdateView, StatusUpdateView)

urlpatterns = [
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/detail/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    path('language/create/', LanguageCreateView.as_view(), name='language-create'),
    path('language/list/', LanguageListView.as_view(), name='language-list'),
    path('language/<int:pk>/update/', LanguageUpdateView.as_view(), name='language-update'),

    path('framework/create/', FrameworkCreateView.as_view(), name='framework-create'),
    path('framework/list/', FrameworkListView.as_view(), name='framework-list'),
    path('framework/<int:pk>/update/', FrameworkUpdateView.as_view(), name='framework-update'),

    path('backend/<int:pk>/create/', LogicalCreateView.as_view(), name='backend-create'),
    path('backend/<int:pk>/update/', LogicalUpdateView.as_view(), name='backend-update'),

    path('frontend/<int:pk>/create/', InterfaceCreateView.as_view(), name='frontend-create'),
    path('frontend/<int:pk>/update/', InterfaceUpdateView.as_view(), name='frontend-update'),

    path('feature/<int:pk>/create/', FeatureCreateView.as_view(), name='feature-create'),
    path('feature/<int:pk>/update/', FeatureUpdateView.as_view(), name='feature-update'),
    path('feature/<int:pk>/list/', FeatureListView.as_view(), name='feature-list'),

    path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
]
