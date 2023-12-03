from django.urls import path, include
from blog.apps import BlogConfig
from blog.view import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView, BlogUpdateView, BlogAllListView, \
    toggle_published

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_all_list/', BlogAllListView.as_view(), name='blog_all_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('published/<int:pk>', toggle_published, name='toggle_published'),
]
