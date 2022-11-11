from rest_framework import serializers
from ...models import Category, Tag, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title')


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    tag_names = serializers.SerializerMethodField(read_only=True, required=False)

    def get_tag_names(self, obj):
        tags = obj.tags.all()
        data = []
        for i in tags:
            data.append({'title': i.title})
        return data

    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'category','category_name', 'image', 'content', 'tags', 'tag_names', 'created_at')

    def create(self, validate_data):
        tags = validate_data.pop('tags')
        user = self.context['request'].user
        blog = Blog.objects.create(author_id=user.id, **validate_data)
        for tag in tags:
            blog.tags.add(tag)

        return blog

