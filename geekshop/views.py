from django.shortcuts import render
from mainapp.models import Product




def index(request):
    title = "GeekShop"

    products = Product.objects.all()[:3]

    context = {
        "title": title,
        "products": products,
    }
    return render(request, 'index.html', context)


def contact(request):
    title = "контакты"

    context = {
        "title": title,

    }
    return render(request, 'contact.html', context)
