from django.urls import path

from product.apps import ProductConfig
from product.views import index, contacts, one

app_name = ProductConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/one/', one, name='one'),

]
