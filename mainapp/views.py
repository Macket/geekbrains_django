from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def main(request):
    context = {'username': 'alexey'}
    return render(request, 'mainapp/main.html', context)


def products(request, pk=None):
    products = Product.objects.all()

    if pk or pk == 0:
        if pk != 0:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category=category)
        context = {'products': products, 'categories': ProductCategory.objects.all()}
        return render(request, 'mainapp/products.html', context)
    else:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {'hot_product': hot_product, 'categories': ProductCategory.objects.all()}
        return render(request, 'mainapp/hot_product.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
