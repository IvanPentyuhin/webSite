from django.shortcuts import render
from mainapp.models import Product


def products(request):

    title = "каталог"
    products = Product.objects.all()[:3]

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},

    ]

    context = {
        "title": title,
        "links_menu": links_menu,
        "products": products,
    }

    return render(request, 'products.html', context)