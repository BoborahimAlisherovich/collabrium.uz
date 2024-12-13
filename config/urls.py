

from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from Collabrium.views import SpaceViewSet,FaqViewSet
from Collabrium.views import OurTeamSerializerViewSet,RezidentSerializerViewSet
from rest_framework.routers import DefaultRouter



schema_view = get_schema_view(
    openapi.Info(
        title="Collabrium.uz",
        default_version='v1',
        description="Restaurants and Stores delivery service",
        contact=openapi.Contact(email="collabrium77@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('spaces',SpaceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('spaces/<int:pk>/', SpaceViewSet.as_view({'get': 'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name='space-detail'),
    path('faqs',FaqViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('faqs/<int:pk>/', FaqViewSet.as_view({'get': 'retrieve' ,'put':'update','patch':'partial_update','delete':'destroy'}), name='faq-detail'),
   

   # Address uchun
path(
    'Rezidents/',
    RezidentSerializerViewSet.as_view({'get': 'list', 'post': 'create'}),
),
path(
    'Rezidents/<int:pk>/',
    RezidentSerializerViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'patch': 'partial_update', 
        'delete': 'destroy'
    }),
),

# PlasticCard uchun
path(
    'OurTeam/',
    OurTeamSerializerViewSet.as_view({'get': 'list', 'post': 'create'}),
),
path(
    'OurTeam/<int:pk>/',
    OurTeamSerializerViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'patch': 'partial_update', 
        'delete': 'destroy'
    }),
),

]

