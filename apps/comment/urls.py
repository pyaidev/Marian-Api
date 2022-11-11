from django.urls import path, include

urlpatterns = [
    path('', include('apps.comment.api.v1.urls'))
]