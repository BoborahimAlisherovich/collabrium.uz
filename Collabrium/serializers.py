from rest_framework import serializers
from .models import OurTeam,Rezident

class RezidentSerializer(serializers.Serializer):
    class Meta:
        model = Rezident
        fields = ["id","name","image","job","description"]

class OurTeamSerializer(serializers.Serializer):
    class Meta:
        model = OurTeam
        fields = ["id","name","image","job","description"]