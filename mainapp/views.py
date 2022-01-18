import random

from django.shortcuts import render, get_object_or_404


from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def get_hot_product():
    product = Product.objects.all()

    return random.sample(list(product), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products


def products(request, pk=None, page=1):

    title = "каталог"
    links_menu = ProductCategory.objects.all()
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    products = Product.objects.all().order_by("price")

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {
                'pk': 0,
                "name": "ВCE"
                }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")

        paginator = Paginator(products, 1)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            "title": title,
            "links_menu": links_menu,
            "products": products_paginator,
            "category": category,
            "hot_product": hot_product,
            "same_products": same_products,
        }

        return render(request, 'products.html', context)

    context = {
        "title": title,
        "links_menu": links_menu,
        "hot_product": hot_product,
        "same_products": same_products,
        "products": products,
    }

    return render(request, 'products.html', context)


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'product_details.html', context)
