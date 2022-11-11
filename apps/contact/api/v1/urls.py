from django.urls import path, include
from .views import ContactApiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactApiViewSet)
urlpatterns = [
    path('', include(router.urls)),
]