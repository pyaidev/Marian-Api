from rest_framework import status, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    # http://127.0.0.1:8000/api/blog/v1/blog-list-create/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['id', 'title', 'created_at']
    # search_fields = ['id', 'title', 'created_at', 'tags']

    def get_queryset(self):
        queryset = Blog.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title,)
        return queryset
    # permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated, permissions.IsAdminUser]


class BlogRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<int:pk>/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnUserOrReadOnly,  permissions.IsAuthenticated, permissions.IsAdminUser]

