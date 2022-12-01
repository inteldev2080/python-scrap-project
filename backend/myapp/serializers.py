from rest_framework import serializers
from .models import CryptoModel


class CryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CryptoModel
        fields = "__all__"