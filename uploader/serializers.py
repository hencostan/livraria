from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'  # ou defina explicitamente os campos, como ['id', 'image']
