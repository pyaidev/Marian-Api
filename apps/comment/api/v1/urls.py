from django.urls import path, include
from .views import CommentListCreateView, CommentDeleteView

urlpatterns = [
    path('<int:post_id>/list-create/', CommentListCreateView.as_view()),
    path('<int:post_id>/delete/<int:pk>/', CommentDeleteView.as_view()),
]