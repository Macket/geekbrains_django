from django.shortcuts import render
from .models import Product


def main(request):
    context = {'username': 'alexey'}
    return render(request, 'mainapp/main.html', context)


def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
