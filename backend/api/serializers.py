from rest_framework import serializers
from .models import ContentBlock

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'

