from rest_framework import viewsets
from .serializers import ContactSerializer
from ...models import Contact


class ContactApiViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/contact/contacts/<id>
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post']