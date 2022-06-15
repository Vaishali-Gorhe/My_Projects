from rest_framework import serializers
from .models import DIM_USER


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DIM_USER
        fields = ('__all__')
        