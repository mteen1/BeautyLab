from django.urls import path

from .views import hair_product_list

urlpatterns = [
    path("hair-products/", hair_product_list, name="hair-products")
]
