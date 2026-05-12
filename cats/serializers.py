from rest_framework import serializers
from .models import Cat

# Serializers convert model instances to JSON.
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
