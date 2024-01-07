import random

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.config import symbols
from users.forms import UserRegisterForm, UserForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        self.object=form.save()

        # symbols

        send_mail(
            subject='Верификация почты на сайте "Продуктовый магазин"',
            message=f'Для регистрации на сайте необходимо пройти по ссылке: {symbols}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )

class UserUpdateView(UpdateView):
    model = UserRegisterForm
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

def gen_pasw(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    send_mail(
        subject='Сгенерирован новый пароль',
        message=f'Ваш новый пароль: {new_password} ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('product:index'))
