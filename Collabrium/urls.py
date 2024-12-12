from django.urls import path
from .views import SpaceListCreateView, SpaceDetailView,FaqListCreateView, FaqDetailView
from .views import schema_view

urlpatterns = [
    path('spaces/', SpaceListCreateView.as_view(), name='space-list-create'),
    path('spaces/<slug:slug>/', SpaceDetailView.as_view(), name='space-detail'),
    path('faqs/', FaqListCreateView.as_view(), name='faq-list-create'),  
    path('faqs/<slug:slug>/', FaqDetailView.as_view(), name='faq-detail'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
