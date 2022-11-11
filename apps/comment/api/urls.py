from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.comment.api.v1.urls'))
]