from rest_framework import serializers
                           

from .models import Property

from useraccount.serializers import UserDetailSerializer

class PropertiesListSerializer(serializers.ModelSerializer):
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
            'title',
            'description',
            'price_per_night',
            'imagen_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
        )


class ReservationsListSerializer(serilizers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)
    
    class meta:
        model = Reservation
        fields = (
            'id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'property'
        )