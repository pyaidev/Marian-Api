from django.urls import path
from .views import ServiceListView, RoomsListView, RoomsCreateView, ServiceCreateView, ServiceRetriveUpdateDestroyView


urlpatterns = [
    path('service-list/', ServiceListView.as_view()),
    path('service-create/', ServiceCreateView.as_view()),
    path('service-rud/<int:pk>/', ServiceRetriveUpdateDestroyView.as_view()),
    path('room-list/', RoomsListView.as_view()),
    path('room-create/', RoomsCreateView.as_view()),
]