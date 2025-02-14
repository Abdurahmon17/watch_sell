from django.urls import path
from .views import register_user, login_user, logout_user, forgot_password, verify_reset_code, reset_password_done

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('auth/forgot-password/', forgot_password, name='forgot_password'),
    path('auth/verify-reset-code/', verify_reset_code, name='verify_reset_code'),
    path('auth/reset-password-done/', reset_password_done, name='reset_password_done'),
]




