from rest_framework import serializers
from ...models import Service, Room, Booking
from apps.wallet.models import Wallet


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
        fields = ['user', 'email', 'phone', 's_d', 'e_d', 'package']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     booking = Booking.objects.create(user_id=user.id, **validated_data)
    #     return booking

    def validate(self, attrs):
        attrs = dict(attrs)
        room = Room.objects.get(title=attrs.get('package'))
        obj = Wallet.objects.get(author=self.context['request'].user)
        booking_room = Booking.objects.filter(show=True).filter(package_id=room.id)
        if booking_room.count():
            raise serializers.ValidationError({"room": "you already booking"})

        if room.price > obj.balance:
            raise serializers.ValidationError({"money": "you don't have enough money"})
        elif room.price == obj.balance:
            obj.balance = 0
        else:
            obj.balance -= room.price // 2
        obj.save()
        attrs['user'] = obj.author
        return attrs
