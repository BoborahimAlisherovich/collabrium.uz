from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import RezidentSerializer,OurTeamSerializer
from .models import Rezident
from rest_framework import status
from rest_framework import permissions

from .models import Space,Faq,OurTeam,Rezident



class OurTeamSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return OurTeam.objects.filter(name=self.request.user.username)


class RezidentSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = RezidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rezident.objects.filter(name=self.request.user.username)

  