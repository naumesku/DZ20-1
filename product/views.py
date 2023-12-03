from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductListView(ListView):
    model = Product
    # template_name = 'product/product_list.html'

# Create your views here.
# def index(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Продукты'
#     }
#     return render(request, 'product/product_list.html', context)


def contacts(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'product/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product

# def one(request, pk):
#     product_name = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'{product_name.name}'
#     }
#     return render(request, 'product/product_detail.html', context)


