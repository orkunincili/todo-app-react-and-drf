from rest_framework import serializers
from todo import models




class TodoSerializer(serializers.ModelSerializer):
    """Serializes todos"""

    class Meta:
        model = models.Todo
        fields = '__all__'
