from django.shortcuts import render

from product.models import Product


# Create your views here.
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'products/index.html', context)


def contacts(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'products/contacts.html', context)



def one(request, pk):
    product_name = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'{product_name.name}'
    }
    return render(request, 'products/one.html', context)
