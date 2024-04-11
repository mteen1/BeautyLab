from django.contrib import admin

from .models import Product 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','draft',)
    list_filter = ('draft',)

admin.site.register(Product, ProductAdmin)
