import json, os
from django.shortcuts import render
from mainapp.models import Product
links_menu = [{'href': '/', 'name': 'Home'},{'href': '/catalog/', 'name': 'Catalog'},{'href': '/contacts/',
                                                                                      'name': 'Contacts'}]


def main(request):
    return render(request, 'mainapp/index.html', context={'title': 'Home','content': links_menu })



def catalog(request):
    content = {'title': 'Catalog', 'products': [{'name': 'Evolution with Arsen', 'link': '../static/img/product1.html',
                                                 'img': '../static/img/evolution_from_arsen.png'
                                                 },
                                                {'name': 'Evolution with Mark', 'link': '../static/img/product2.html',
                                                 'img': '../static/img/evolution_from_mark.jpg'
                                                 }],'content': links_menu
               }
    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'contacts','content': links_menu })


def product(request):
    return render(request, 'mainapp/product.html', context={'title': 'Product', 'products':Product.objects.all,
                                                            'content': links_menu })


