from django.contrib import admin
from django.urls import path, include
from products.api import router as product_router
from accounts.api import router as account_router

from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI

api = NinjaAPI()
api.add_router('/products/', product_router)
api.add_router("/accounts/", account_router)




urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
