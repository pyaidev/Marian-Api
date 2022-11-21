from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from apps.marian.models import Booking
from ...models import Wallet
from .serializers import WalletSerializer
from apps.accounts.api.v1.permissions import IsOwnUserOrReadOnly


class Balance(generics.ListAPIView):
    queryset = Wallet
    serializer_class = WalletSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)
