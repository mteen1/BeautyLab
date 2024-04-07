from django.urls import path
from .views import HairProductView, DetailHairProductView


urlpatterns = [
    path("<int:pk>/", DetailHairProductView.as_view(), name="hairproduct_detail"),
    path("", HairProductView.as_view(), name="hairproduct_list"),
]
