from rest_framework import generics
from .models import HairProduct
from .serializers import HairProductSerializer


class HairProductView(generics.ListAPIView):
    queryset = HairProduct.objects.all()
    serializer_class = HairProductSerializer


class DetailHairProductView(generics.RetrieveAPIView):
    queryset = HairProduct.objects.all()
    serializer_class = HairProductSerializer