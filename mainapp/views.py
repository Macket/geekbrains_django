from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/main.html', {'username': 'alexey', 'array': [1, 2, 3, 4, 5]})


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
