from rest_framework import serializers
from .models import Birthday

class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'birthday',
            'user',
        )
        model = Birthday