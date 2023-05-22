
from django.urls import path 

from . import views

from django.contrib.auth import views as auth_views

app_name ="users_app"


urlpatterns = [
    path('registro/', views.UserRegisterView.as_view(),name='user_register'),
    path('login/', views.LoginUser.as_view(),name='user_login'),
    path('logout/', views.LogoutView.as_view(),name='user_logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]