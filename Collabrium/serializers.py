from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq, Blog, Jihoz,Tarif,Plansedescription
from rest_framework import serializers


class PlansedescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plansedescription
        fields = ['id', 'description','description_uz','description_en','description_ru']


class TariffSerializer(serializers.ModelSerializer):
    services = PlansedescriptionSerializer(
        many=True, 
        source='Plansedescriptions',  # Matches the related_name in the ManyToManyField
        read_only=True
    )
    space_slug = serializers.CharField(source='space.page_slug', read_only=True)

    class Meta:
        model = Tarif
        fields = ['id', 'name','name_uz','name_en','name_ru', 'price', 'duration','duration_uz','duration_en','duration_ru', 'space_slug','services']



class JihozSerializer(serializers.ModelSerializer):
    equipment_uz = serializers.CharField(source='total_uz') 
    equipment_en = serializers.CharField(source='total_en')  
    equipment_ru = serializers.CharField(source='total_ru')  

    class Meta:
        model = Jihoz
        fields = [
            'id',
            'equipment_uz',
            'equipment_en',
            'equipment_ru',
            'image'
        ]


class SpaceSerializer(serializers.ModelSerializer):
    equipments = JihozSerializer(many=True, source='jihozlar') 
    plans = TariffSerializer(many=True, source='tariflar', read_only=True)

    class Meta:
        model = Space
        fields = [
                'id', 
                'space_uz', 
                'space_en', 
                'space_ru', 
                'page_slug', 
                'image',
                'equipments',
                'plans',
        ]


class FaqSerializer(serializers.ModelSerializer):
    space = serializers.CharField(source='space.space', read_only=True)

    class Meta:
        model = Faq
        fields = [
            'id', 
            'title_uz', 
            'title_en', 
            'title_ru', 
            'text_uz', 
            'text_en', 
            'text_ru',
            'page_slug',
            'space'
            ]
    
    def create(self, validated_data):
        return Faq.objects.create(**validated_data)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'image_cover',
            'date',
            'title_uz',
            'title_en',
            'title_ru',
            'page_slug',
            'main_title_uz',
            'main_title_en',
            'main_title_ru',
            'text_first_uz',
            'text_first_en',
            'text_first_ru',
            'text_second_uz',
            'text_second_en',
            'text_second_ru',
            'image_first',
            'image_second'
        ]
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "created_at",
        ]



class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = [
            'id',
            'name_uz',
            'name_en',
            'name_ru',
            'image',
            'job_uz',
            'job_en',
            'job_ru',
            'description_uz',
            'description_en',
            'description_ru',
        ]

    def create(self, validated_data):
        return OurTeam.objects.create(**validated_data)

class RezidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezident
        fields = [
            'id',
            'name_uz',
            'name_en',
            'name_ru',
            'job_uz',
            'job_en',
            'job_ru',
            'description_uz',
            'description_en',
            'description_ru',
        ]

    def create(self, validated_data):
        return Rezident.objects.create(**validated_data)
