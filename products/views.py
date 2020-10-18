from django.shortcuts import render
from .models import Wine


def all_wines(request):
    """ A view to return all wines, including sorting and search queries """

    products = Wine.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
