from django.shortcuts import render
from .models import HairProduct


def hair_product_list(request):
    """
    Function-based view to list all HairProduct objects.
    """
    # Fetch all HairProduct objects from the database
    hair_products = HairProduct.objects.all()

    # Context dictionary to pass data to the template
    context = {"hair_products": hair_products}

    # Render the hair_product_list.html template with the context
    return render(request, "hair_product_list.html", context)
