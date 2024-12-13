from rest_framework import serializers
from .models import OurTeam,Rezident,Space,Faq


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'space'):
            validated_data['space'] = request.space 
        return super().create(validated_data)



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
        fields = ['id', 'title', 'text', 'page_slug']
    
    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'faq'):
            validated_data['faq'] = request.faq 
        return super().create(validated_data)



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

