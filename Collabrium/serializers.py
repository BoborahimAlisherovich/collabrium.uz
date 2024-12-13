from rest_framework import serializers
from .models import OurTeam,Rezident
from .models import Space,Faq


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'space', 'page_slug', 'image']

    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'space'):
            validated_data['space'] = request.space 
        return super().create(validated_data)



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'title', 'text', 'page_slug']
    
    def create(self, validated_data):
        request = self.context.get('request')  
        if request and hasattr(request, 'faq'):
            validated_data['faq'] = request.faq 
        return super().create(validated_data)








        
class RezidentSerializer(serializers.Serializer):
    class Meta:
        model = Rezident
        fields = ["id","name","image","job","description"]

class OurTeamSerializer(serializers.Serializer):
    class Meta:
        model = OurTeam
        fields = ["id","name","image","job","description"]