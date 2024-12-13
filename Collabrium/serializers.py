from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq, Blog


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



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id', 
            'image_cover', 
            'date', 
            'title', 
            'page_slug', 
            'main_title',
            'text_first', 
            'text_second', 
            'image_first', 
            'image_second'
        ]
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)