from django.shortcuts import render, get_object_or_404
from .models import Wine


def all_wines(request):
    """ A view to return all wines, including sorting and search queries """

    products = Wine.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def wine_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Wine, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
