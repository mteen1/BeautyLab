from rest_framework import serializers

from products.models import HairProduct


class HairProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the HairProduct model.
    """

    class Meta:
        model = HairProduct
        fields = "__all__"  # Include all fields by default
        # OR
        # Explicitly define the fields you want to include (optional)
        # fields = (
        #     'name',
        #     'brand',
        #     'description',
        # .
        # .
        # .
        # )
