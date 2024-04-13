from ninja import Router
from .models import Product
from .schemas import ProductOut,ProductDetailOut, ProductCreateSchema
from django.shortcuts import get_object_or_404

router = Router()


@router.get("", response=list[ProductOut])
def get_products(request):
    return Product.objects.filter(draft=False)


@router.get("{slug}/", response=ProductDetailOut)
def get_product(request, slug: str):
    product = get_object_or_404(Product, slug=slug, draft=False)
    return product

@router.post("", response=ProductDetailOut)
def create_product(request, product: ProductCreateSchema):
    product_data = product.model_dump()
    product_obj =Product.objects.create(draft=True,**product_data)
    return product_obj

