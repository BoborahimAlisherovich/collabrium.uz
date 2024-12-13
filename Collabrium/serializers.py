from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = '__all__'

    def create(self, validated_data):
        return Space.objects.create(**validated_data)



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
        fields = ['id', 'title', 'text', 'page_slug']
    
    def create(self, validated_data):
        return Faq.objects.create(**validated_data)




class RezidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezident
        fields = ['id', 'name', 'job', 'description', 'image']

    def create(self, validated_data):
        return Rezident.objects.create(**validated_data)


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'name', 'job', 'description', 'image']

    def create(self, validated_data):
        return OurTeam.objects.create(**validated_data)

