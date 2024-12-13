
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpaceViewSet, FaqViewSet


router= DefaultRouter()
router.register(r'spaces', SpaceViewSet, basename='space')
router.register(r'faqs', FaqViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls)), 
]
