from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import RezidentSerializer,OurTeamSerializer
from rest_framework import permissions

from .models import Space,Faq,OurTeam,Rezident

from .models import Space,Faq
from .serializers import SpaceSerializer,FaqSerializer


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

  