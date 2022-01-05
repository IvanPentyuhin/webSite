import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    product = Product.objects.all()

    return random.sample(list(product), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products


def products(request, pk=None):

    title = "каталог"
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    products = Product.objects.all().order_by("price")

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "ВCE"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")

        context = {
            "title": title,
            "links_menu": links_menu,
            "products": products,
            "category": category,
            "hot_product": hot_product,
            "basket": basket,
            "same_products": same_products,
        }

        return render(request, 'products.html', context)


    context = {
        "title": title,
        "links_menu": links_menu,
        "hot_product": hot_product,
        "basket": basket,
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
        'basket': get_basket(request.user),
    }

    return render(request, 'product_details.html', context)