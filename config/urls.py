from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

from Collabrium.views import (
    SpaceViewSet,
    FaqViewSet,
    OurTeamSerializerViewSet,
    RezidentSerializerViewSet,
    BlogViewSet,
    TariffListView,
 
)

schema_view = get_schema_view(
    openapi.Info(
        title="Collabrium API",
        default_version='v1',
        description="API documentation for the Collabrium platform.",
        contact=openapi.Contact(email="collabrium77@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("_admin-qw4r56/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),


    # Spaces
    path("spaces/", SpaceViewSet.as_view({'get': 'list'})),
    path("spaces/<int:pk>/", SpaceViewSet.as_view({'get': 'retrieve'}), name="space-detail"),

    # FAQs
    path("faqs/", FaqViewSet.as_view({'get': 'list'})),
    path("faqs/<int:pk>/", FaqViewSet.as_view({'get': 'retrieve'}), name="faq-detail"),

    # Residents
    path("rezidents/", RezidentSerializerViewSet.as_view({'get': 'list'})),
    path("rezidents/<int:pk>/", RezidentSerializerViewSet.as_view({'get': 'retrieve'}), name="rezident-detail"),

    # Our Team
    path("ourteam/", OurTeamSerializerViewSet.as_view({'get': 'list'})),
    path("ourteam/<int:pk>/", OurTeamSerializerViewSet.as_view({'get': 'retrieve'}), name="ourteam-detail"),

    # Blog
    path("blog", BlogViewSet.as_view({'get': 'list'}), name="blog-details"),
    path("blog/<int:pk>/", BlogViewSet.as_view({'get': 'retrieve'}), name="blog-detail"),
   

    # Tariff
    path("tariffs/", TariffListView.as_view({'get': 'list'})),
    path("tariffs/<int:pk>/", TariffListView.as_view({'get': 'retrieve'}), name="tariff-detail"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
