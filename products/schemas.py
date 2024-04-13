from ninja import ModelSchema, Schema
from .models import Product, SkinConcern, Ingredient


class ProductOut(ModelSchema):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "slug")

class ProductDetailOut(ModelSchema):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ("id", "name", "description","skin_type","ingredients", "slug")


class ProductCreateSchema(Schema):
    name: str
    description: str | None = None
    ingredients: str
    skin_type: str | None = None
