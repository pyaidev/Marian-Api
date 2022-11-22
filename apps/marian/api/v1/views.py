from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics,permissions, status
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnUserOrReadOnly
from ...models import Service, Room, Booking
from .serializers import ServiceSerializer, RoomSerializer, BookingSerializer


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


# class BookingCreateAPIView(generics.CreateAPIView):
#     # http://127.0.0.1:8000/api/marian/booking/<int:pk>/
#     permission_classes=[IsAuthenticated]
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
    #
    # def perform_create(self, serializer):
    #
    #     # user = self.request.user
    #     package = get_object_or_404(Room, pk= self.kwargs['pk'])
    #     serializer.save(user=self.request.user, package=package)
    #
    # def get(self, request):
    #     bookings = Booking.objects.get(user=request.user)
    #     return HttpResponse(bookings)


class BookFilter(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/marian/booking/
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(BookFilter, self).get_queryset()
        a = self.request.POST.get('a')
        b = self.request.POST.get('b')
        print(a)
        print(b)
        print(qs)
        if a and b:
            qs = qs.filter(~Q(s_d__range=[a, b]) or ~Q(e_d__range=[a, b]))
        return qs

    def perform_create(self, serializer):
        serializer = self.serializer_class(data=self.request.data, context={"request": self.request})
        room = Room.objects.get(id=self.request.POST.get('package'))
        room.empty = True
        room.check_in = self.request.POST.get('start_day')
        room.check_out = self.request.POST.get('end_day')
        author_id = self.request.user.id
        print(author_id)
        if serializer.is_valid():
            serializer.save(package=room, user_id=author_id)
            room.save()


