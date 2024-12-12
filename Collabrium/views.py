from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .serializers import RezidentSerializer,OurTeamSerializer
from .models import Rezident
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Space,Faq
from .serializers import SpaceSerializer,FaqSerializer



class SpaceListCreateView(APIView):
    def get(self, request):
        spaces = Space.objects.all()
        serializer = SpaceSerializer(spaces, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SpaceDetailView(APIView):
    def get(self, request, slug):
        try:
            space = Space.objects.get(page_slug=slug)
            serializer = SpaceSerializer(space)
            return Response(serializer.data)
        except Space.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            space = Space.objects.get(page_slug=slug)
            serializer = SpaceSerializer(space, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Space.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug):
        try:
            space = Space.objects.get(page_slug=slug)
            space.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Space.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)





class FaqListCreateView(APIView):
    def get(self, request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FaqDetailView(APIView):
    def get(self, request, slug):
        try:
            faq = Faq.objects.get(page_slug=slug)
            serializer = FaqSerializer(faq)
            return Response(serializer.data)
        except Faq.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            faq = Faq.objects.get(page_slug=slug)
            serializer = FaqSerializer(faq, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Faq.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug):
        try:
            faq = Faq.objects.get(page_slug=slug)
            faq.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Faq.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)



class OurTeamSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class RezidentSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = RezidentSerializer
    permission_classes = [permissions.IsAuthenticated]

   
    def get_queryset(self):
        return Rezident.objects.filter(user=self.request.user)

  