from rest_framework import generics
from .models import HairProduct
from .serializers import HairProductSerializer


class HairAPIView(generics.ListAPIView):
    queryset = HairProduct.objects.all()
    serializer_class = HairProductSerializer
