from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Wine, WineType, Region, Winery


def all_wines(request):
    """ A view to return all wines, including sorting and search queries """

    products = Wine.objects.all()
    query = None
    wine_types = None
    regions = None
    wineries = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            print(sortkey)
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'wine_type' in request.GET:
            wine_types = request.GET['wine_type']
            products = products.filter(wine_type__name=wine_types)
            wine_types = WineType.objects.filter(name__in=wine_types)

        if 'region' in request.GET:
            regions = request.GET['region']
            products = products.filter(region__name=regions)
            regions = Region.objects.filter(name__in=regions)

        if 'winery' in request.GET:
            wineries = request.GET['winery']
            products = products.filter(winery__name=wineries)
            wineries = Winery.objects.filter(name__in=wineries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_wine_types': wine_types,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Wine, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
