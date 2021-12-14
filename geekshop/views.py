from django.shortcuts import render


def index(request):
    title = "GeekShop"
    index = "index"
    contact = "contact"
    products = "products"
    menu = [
        {'href': index, 'name': 'домой'},
        {'href': products, 'name': 'продукты'},
        {'href': contact, 'name': 'контакты'},
    ]
    context = {
        "title": title,
        "menu": menu,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    title = "контакты"
    index = "index"
    products = "products"
    contact = "contact"
    menu = [
        {'href': index, 'name': 'домой'},
        {'href': products, 'name': 'продукты'},
        {'href': contact, 'name': 'контакты'},
    ]
    context = {
        "title": title,
        "menu": menu,
    }
    return render(request, 'contact.html', context=context)
