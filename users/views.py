import random
from django.core.signing import BadSignature, Signer
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.config import symbols
from users.forms import UserRegisterForm, UserForm
from users.models import User
from users.utils import token_generate, email_token


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object=form.save()

        key, token = token_generate(self.object.email)
        verification_link = f'http://127.0.0.1:8000/users/verify_email/{token}'
        self.object.token = key
        self.object.save()

        send_mail(
            subject='Верификация почты на сайте "Продуктовый магазин"',
            message=f'Для регистрации на сайте необходимо пройти по ссылке: {verification_link}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )
        return redirect('users:confirm_email')

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

def email_verify(request, token):
    key_from_token, email_from_token = email_token(token)
    user = get_object_or_404(User, email=email_from_token)
    # Получаем пользователя

    if str(user.token) == str(key_from_token):
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))
