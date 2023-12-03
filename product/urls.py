from django.urls import path

from blog.view import BlogListView
from product.apps import ProductConfig
from product.views import contacts, ProductListView, ProductDetailView

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/view/', ProductDetailView.as_view(), name='product_details'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
]
