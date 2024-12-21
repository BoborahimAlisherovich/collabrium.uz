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


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Faq.objects.filter()


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

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        # Query param dan 'limit' ni olish, default 10 ta blog qaytariladi
        limit = request.query_params.get('limit', 10)
        try:
            limit = int(limit)  # Limitni son turiga o'zgartirish
            if limit <= 0:  # Manfiy yoki 0 bo'lsa, noto'g'ri qiymat xabari
                return Response(
                    {"error": "Limit must be a positive integer."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {"error": "Limit must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Bloglarni olish
        blogs = Blog.objects.all().order_by('-date')[:limit]
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)