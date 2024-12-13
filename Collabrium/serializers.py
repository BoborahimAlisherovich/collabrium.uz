from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'space', 'page_slug', 'image']

    def create(self, validated_data):
        # Qo'shimcha o'zgartirishlar kerak bo'lsa, bu yerda amalga oshiring
        return Space.objects.create(**validated_data)



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'title', 'text', 'page_slug']
    
    def create(self, validated_data):
        #salom
        return Faq.objects.create(**validated_data)



from rest_framework import serializers
from .models import Rezident, OurTeam

class RezidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezident
        fields = ['id', 'name', 'job', 'description', 'image']

    def create(self, validated_data):
        # Qo'shimcha o'zgartirishlar kerak bo'lsa, bu yerda amalga oshiring
        return Rezident.objects.create(**validated_data)


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'name', 'job', 'description', 'image']

    def create(self, validated_data):
        # Qo'shimcha o'zgartirishlar kerak bo'lsa, bu yerda amalga oshiring
        return OurTeam.objects.create(**validated_data)

