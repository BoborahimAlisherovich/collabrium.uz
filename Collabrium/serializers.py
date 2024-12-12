from rest_framework import serializers
from .models import OurTeam,Rezident
from rest_framework import serializers
from .models import Space,Faq

class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'space', 'page_slug', 'image']



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'title', 'text', 'page_slug']








        
class RezidentSerializer(serializers.Serializer):
    class Meta:
        model = Rezident
        fields = ["id","name","image","job","description"]

class OurTeamSerializer(serializers.Serializer):
    class Meta:
        model = OurTeam
        fields = ["id","name","image","job","description"]