from rest_framework import serializers
from ...models import Service, Room, Booking


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def validate_title(self, attrs):
        user = self.context['request'].user
        posts = Service.objects.filter(title__icontains=attrs, author_id=user.id)
        if posts:
            raise serializers.ValidationError('Sizda bu title oldin qoshilgan')
        return attrs


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = ['user', 'name', 'email', 'phone', 's_d', 'e_d', 'package']

    def create(self, validated_data):
        user = self.context['request'].user
        booking = Booking.objects.create(user_id=user.id, **validated_data)
        return booking

