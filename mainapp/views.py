from django.shortcuts import render



def products(request):

    title = "каталог"
    index = "index"
    contact = "contact"
    products = "products"
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},

    ]

    menu = [
        {'href': index, 'name': 'домой'},
        {'href': products, 'name': 'продукты'},
        {'href': contact, 'name': 'контакты'},
    ]
    context = {
        "title": title,
        "links_menu": links_menu,
        "menu": menu,
    }

    return render(request, 'products.html', context=context)