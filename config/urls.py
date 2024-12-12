

from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from Collabrium.views import OurTeamSerializerViewSet,RezidentSerializerViewSet



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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("api/Rezident/",RezidentSerializerViewSet.as_view({'get':'list'}),name = "rezident")

]
