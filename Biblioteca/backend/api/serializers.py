from rest_framework import serializers

from .models import Prestamos


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'
