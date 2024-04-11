from ninja import ModelSchema, Schema
from .models import Product


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "ingredients", "skin_type", "slug")


class ProductCreateSchema(Schema):
    name: str
    description: str | None = None
    ingredients: str
    skin_type: str | None = None
