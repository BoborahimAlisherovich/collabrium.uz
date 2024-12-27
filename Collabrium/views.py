from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Space, Faq, OurTeam, Rezident, Blog, Tarif
from .serializers import SpaceSerializer, FaqSerializer, OurTeamSerializer, RezidentSerializer, BlogSerializer, TariffSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    serializer_class = SpaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Space.objects.exclude(page_slug='home')



class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible
    queryset = Faq.objects.all()

    @swagger_auto_schema(
        operation_description="Retrieve a list of FAQs filtered by space_slug.",
        manual_parameters=[
            openapi.Parameter(
                'space_slug', openapi.IN_QUERY, description='Filter FAQs by space_slug.', 
                type=openapi.TYPE_STRING, required=False
            ),
        ],
        responses={200: FaqSerializer(many=True), 404: "No FAQs found for the given space_slug."}
    )
    def list(self, request, *args, **kwargs):
        space_slug = request.query_params.get("space_slug")
        faqs = Faq.objects.filter(space__page_slug=space_slug) if space_slug else Faq.objects.all()

        if not faqs:
            return Response({"error": "No FAQs found for the given space_slug."}, status=status.HTTP_404_NOT_FOUND)

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

    @swagger_auto_schema(
        operation_description="Retrieve tariffs optionally filtered by space slug.",
        manual_parameters=[openapi.Parameter('slug', openapi.IN_QUERY, description="Slug of the space to filter tariffs.", type=openapi.TYPE_STRING)],
        responses={200: TariffSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        slug = request.query_params.get("slug")
        queryset = self.get_queryset()

        if slug:
            queryset = queryset.filter(space__page_slug=slug)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of blogs with an optional limit on the number of blogs returned. Defaults to 10.",
        manual_parameters=[openapi.Parameter('limit', openapi.IN_QUERY, description='Optional limit on the number of blogs to retrieve.', type=openapi.TYPE_INTEGER)],
        responses={200: BlogSerializer(many=True), 400: "Limit must be a positive integer."}
    )
    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', 10)

        try:
            limit = int(limit)
            if limit <= 0:
                raise ValueError
        except ValueError:
            return Response(
                {"error": "Limit must be a positive integer.", "usage": "Example: ?limit=5"},
                status=status.HTTP_400_BAD_REQUEST
            )

        blogs = Blog.objects.all().order_by('-id')[:limit]
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
