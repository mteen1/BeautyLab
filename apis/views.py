from rest_framework import generics

from products.models import HairProduct
from .serializers import HairProductSerializer

class HairAPIView(generics.ListAPIView):
    queryset = HairProduct.objects.all()
    serializer_class = HairProductSerializer