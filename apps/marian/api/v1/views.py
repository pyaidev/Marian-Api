from rest_framework import generics,permissions

from .permissions import IsOwnUserOrReadOnly
from ...models import Service, Room
from .serializers import ServiceSerializer, RoomSerializer


class ServiceListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/marian/v1/service-list/
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreateView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/marian/v1/service-create/
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated]


class RoomsListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/marian/v1/room-list/
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomsCreateView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/marian/v1/room-create/
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated]


class ServiceRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/marian/service-rud/<int:pk>/
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnUserOrReadOnly, permissions.IsAuthenticated]

