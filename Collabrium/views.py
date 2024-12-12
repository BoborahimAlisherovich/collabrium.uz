from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .serializers import RezidentSerializer,OurTeamSerializer
from .models import Rezident


class OurTeamSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class RezidentSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = RezidentSerializer
    permission_classes = [permissions.IsAuthenticated]

   
    def get_queryset(self):
        return Rezident.objects.filter(user=self.request.user)

  