from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework import permissions
from .serializers import RezidentSerializer,OurTeamSerializer, SpaceSerializer,FaqSerializer, BlogSerializer,TariffSerializer
from .models import Space,Faq,OurTeam,Rezident, Blog,Tarif
from rest_framework.response import Response


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
# Tariff View



class TariffListView(viewsets.ModelViewSet):

    queryset = Tarif.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        slug = self.request.query_params.get("slug")  # Space slug'ini olish
        if slug:
            return self.queryset.filter(space__slug=slug)
        return self.queryset
  
    
class BlogViewSet(viewsets.ModelViewSet):
   
    queryset = Blog.objects.all().order_by("-date")
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


    
from rest_framework import status
from rest_framework.views import APIView

class LatestThreeBlogsView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.order_by('-date')[:3]  # Oxirgi 3 blogni chiqaradi
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllBlogsView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-date')  # Hammasini chiqaradi
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)