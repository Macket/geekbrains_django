from django.shortcuts import render

def index(request):
    title_name = 'Личный сайт для тестов'
    description = "Личный сайт для тестов: новости и примеры работ."

    context = {'set_title':title_name,'description':description}
    return render(request, 'index.html',context)

def product_list(request):
    title_name = 'Каталог товаров'
    description = "Личный сайт для тестов: новости и примеры работ. Каталог товаров."
    
    context = {'set_title':title_name,'description':description}
    return render(request, 'product_list.html',context)

def product_detail(request):
    title_name = 'Товар детально'
    


    description = 'Личный сайт для тестов: новости и примеры работ. Детальный просмотр позиции каталога.'
    context = {'set_title':title_name,'description':description}
    return render(request, 'product_detail.html',context)
