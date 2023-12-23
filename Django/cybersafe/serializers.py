from rest_framework import serializers
from cybersafe.models import Questions


class Questions_serializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'question', 'answer')
    
    