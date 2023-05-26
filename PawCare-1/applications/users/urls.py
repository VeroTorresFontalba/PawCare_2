
from django.urls import path 

from . import views

from django.contrib.auth import views as auth_views

from .forms import UserPasswordResetForm

app_name ="users_app"


urlpatterns = [
    path('registro/', views.UserRegisterView.as_view(),name='user_register'),
    path('login/', views.LoginUser.as_view(),name='user_login'),
    path('logout/', views.LogoutView.as_view(),name='user_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=UserPasswordResetForm), name='password_reset'),
]