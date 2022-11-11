from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.db.models import Q

from .permissions import IsOwnUserOrReadOnly
from ...models import Category, Tag, Blog
from .serializers import CategorySerializer, TagSerializer, BlogSerializer


class CategoryListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/category-list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/tag-list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BloglistView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/blog-list-create/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<int:pk>/'
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated]

