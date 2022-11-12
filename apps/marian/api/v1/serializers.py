from rest_framework import serializers
from ...models import Service, Room


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
