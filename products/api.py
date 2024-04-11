from ninja import NinjaAPI
from .models import Product
from .schemas import ProductSchema, ProductCreateSchema
from django.shortcuts import get_object_or_404

app = NinjaAPI()


@app.get("products/", response=list[ProductSchema])
def get_products(request):
    return Product.objects.all(draft=False)


@app.get("products/{slug}/", response=ProductSchema)
def get_product(request, slug: str):
    product = get_object_or_404(Product, slug=slug, draft=False)
    return product

@app.post("products/", response=ProductSchema)
def create_product(request, product: ProductCreateSchema):
    product_data = product.model_dump()
    product_obj =Product.objects.create(draft=True,**product_data)
    return product_obj

