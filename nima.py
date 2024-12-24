from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from .models import Faq
from .serializers import FaqSerializer

class FaqViewSet(viewsets.ModelViewSet):
    # Define a default queryset to be used if no filtering occurs
    queryset = Faq.objects.all()  # Fallback queryset
    serializer_class = FaqSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible

    # Swagger documentation for the "space_slug" query parameter
    @swagger_auto_schema(
        operation_description="Retrieve a list of FAQs filtered by space_slug.",
        manual_parameters=[
            openapi.Parameter(
                'space_slug', 
                openapi.IN_QUERY, 
                description='Filter FAQs by space_slug. Optional. Example: ?space_slug=example_space',
                type=openapi.TYPE_STRING,
                required=False  # space_slug is optional
            ),
        ],
        responses={
            200: FaqSerializer(many=True), 
            404: "No FAQs found for the given space_slug."
        }
    )
    def get_queryset(self):
        # Get the 'space_slug' query parameter
        space_slug = self.request.query_params.get("space_slug")

        if space_slug:
            # Filter FAQs by space_slug if provided
            return Faq.objects.filter(space__page_slug=space_slug)
        return Faq.objects.all()  # Return all FAQs if no space_slug is provided

    # You can still override `list()` if you need to customize the response handling
    # but in this case, get_queryset() handles the filtering already
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
