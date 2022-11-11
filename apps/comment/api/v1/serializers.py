from rest_framework import serializers
from ...models import Comment


class CommentSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'parent', 'message', 'is_reply', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        try:
            comments = Comment.objects.filter(top_level_comment_id=obj.id).exclude(id=obj.id)
        except:
            return []
        else:
            serializer = CommentSubSerializer(comments, many=True)
            return serializer.data

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'parent', 'post', 'top_level_comment_id', 'message', 'is_reply', 'children', 'created_at')
        extra_kwargs = {
            'author': {'required': False, 'allow_null': True},
            'parent': {'required': False, 'allow_null': True},
            'post': {'required': False, 'allow_null': True},
            'top_level_comment_id': {'required': False, 'allow_null': True, 'read_only': True},
            'is_reply': {'required': False, 'allow_null': True, 'read_only': True},
            'created_at': {'required': False, 'allow_null': True},
        }

