from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from users.apps import UsersConfig
from django.urls import path
from users.views import RegisterView, UserUpdateView, gen_pasw, email_verify

app_name = UsersConfig.name


urlpatterns =[
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/gen_pasw/', gen_pasw, name='gen_pasw'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('verify_email/<str:token>', email_verify, name='verify_email'),

]
