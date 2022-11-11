from django.urls import path, include
from .views import CategoryListView, BloglistView, BlogRetriveUpdateDestroyView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('blog-list-create/', BloglistView.as_view()),
    path('blog-rud/<int:pk>/', BlogRetriveUpdateDestroyView.as_view())
]