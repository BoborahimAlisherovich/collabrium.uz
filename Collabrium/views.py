from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework import permissions
from .serializers import RezidentSerializer,OurTeamSerializer, SpaceSerializer,FaqSerializer, BlogSerializer,TariffSerializer
from .models import Space,Faq,OurTeam,Rezident, Blog,Tarif
from rest_framework.response import Response
from rest_framework import status

class SpaceViewSet(viewsets.ModelViewSet):
    serializer_class = SpaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Space.objects.filter()
    

from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from .models import Faq
from .serializers import FaqSerializer

class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible
    queryset = Faq.objects.all()  # Fallback queryset


    # Swagger documentation for the "space_slug" query parameter
    @swagger_auto_schema(
        operation_description="Retrieve a list of FAQs filtered by space_slug.",
        manual_parameters=[
            openapi.Parameter(
                'space_slug', 
                openapi.IN_QUERY, 
                description='Filter FAQs by space_slug. Optional. Example: ?space_slug=example_space',
                type=openapi.TYPE_STRING,
                required=False
            ),
        ],
        responses={
            200: FaqSerializer(many=True), 
            404: "No FAQs found for the given space_slug."
        }
    )

    def list(self, request, *args, **kwargs):
        # Get the 'space_slug' query parameter
        space_slug = request.query_params.get("space_slug")

        if space_slug:
            faqs = Faq.objects.filter(space__page_slug=space_slug)
        else:
            faqs = Faq.objects.all()

        if not faqs:
            return Response(
                {"error": "No FAQs found for the given space_slug."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize the FAQs and return the response
        serializer = self.get_serializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OurTeamSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return OurTeam.objects.filter()


class RezidentSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = RezidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rezident.objects.filter()
    


class TariffListView(viewsets.ModelViewSet):
    queryset = Tarif.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        slug = self.request.query_params.get("slug")  # Space slug'ini olish
        if slug:
            return self.queryset.filter(space__slug=slug)
        return self.queryset
    permission_classes = [permissions.IsAuthenticated]


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # Swagger documentation for the "limit" query parameter
    @swagger_auto_schema(
        operation_description="Retrieve a list of blogs with an optional limit on the number of blogs returned. Defaults to 10.",
        manual_parameters=[
            openapi.Parameter(
                'limit', 
                openapi.IN_QUERY, 
                description='Optional limit on the number of blogs to retrieve. Must be a positive integer.',
                type=openapi.TYPE_INTEGER
            ),
        ],
        responses={
            200: BlogSerializer(many=True), 
            400: "Limit must be a positive integer."
        }
    )
    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', 10)
        try:
            limit = int(limit)  # Parse the limit
            if limit <= 0:  # Ensure it's positive
                return Response(
                    {
                        "error": "Limit must be a positive integer.",
                        "usage": "Use the 'limit' query parameter to specify how many blogs to retrieve. Example: ?limit=5"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {
                    "error": "Limit must be an integer.",
                    "usage": "Use the 'limit' query parameter to specify how many blogs to retrieve. Example: ?limit=5"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Retrieve blogs with the specified limit
        blogs = Blog.objects.all().order_by('-date')[:limit]
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
