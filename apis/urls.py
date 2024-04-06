from django.urls import path

from .views import HairAPIView

urlpatterns = [
    path("", HairAPIView.as_view(), name="HairProduct_list")
]
