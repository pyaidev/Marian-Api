from rest_framework import status, views, generics, permissions
from rest_framework.response import Response
from ...models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnUserOrReadOnly


class CommentListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/comment/v1/<post_id>/list-create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'post_id'
    pagination_class = None

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(parent__isnull=True)
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        author_id = self.request.user.id
        parent = serializer.validated_data.get('parent', None)
        serializer.save(post_id=post_id, author_id=author_id, parent=parent)


class CommentDeleteView(generics.DestroyAPIView):
    # http://127.0.0.1:8000/api/comment/v1/<post_id>/delete/<comment_id>/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated]