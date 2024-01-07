from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from django.urls import path
from users.views import RegisterView, UserUpdateView, gen_pasw

app_name =UsersConfig.name

urlpatterns =[
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/gen_pasw/', gen_pasw, name='gen_pasw'),
]