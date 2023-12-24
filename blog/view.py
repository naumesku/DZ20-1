from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from pytils.translit import slugify

from blog.models import Blog

class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

class BlogAllListView(ListView):
    model = Blog
    template_name = 'blog/blog_all_list.html'

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'img', 'is_published')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('blog:blog_list', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')



class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'img', 'is_published')
    def get_success_url(self):
        # Получаем значение первичного ключа объекта
        pk = self.object.pk
        # Формируем URL для просмотра отредактированной записи
        return reverse('blog:blog_detail', kwargs={'pk': pk})

def toggle_published(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True

    blog_item.save()

    return redirect(reverse('blog:blog_all_list'))
