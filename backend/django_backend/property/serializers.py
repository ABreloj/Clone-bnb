from rest_framework import serilizers

from .models import Property

from useraccount.serializers import UserDetailSerializer

class PropertiesListSerializer(seriaLizers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )

class PropertiesDetailSerializer(serializers.ModelSerializer):
    landord = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Property
        fields = (
            'id',
            'titulo',
            'descripcion',
            'precio por noche',
            'imagen_url',
            'habitaciones',
            'baños',
            'invitados',
            'landlord'
        )