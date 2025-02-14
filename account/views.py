from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout

def register_user(request):
    if request.user.is_authenticated:  # 🔹 Login bo'lgan foydalanuvchilar kira olmasin
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password1)  # Parolni hashlash
        user.save()
        login(request, user)

        # 📩 Email jo‘natish
        send_mail(
            'Saytimizga Xush kelibsiz!',
            f'Hello {username},\n\nThank you for registering on our site!\n'
            f'Здравствуйте, {username},\n\nСпасибо за регистрацию на нашем сайте!\n'
            f'Salom {username},\n\nSaytimizda roʻyxatdan oʻtganingiz uchun tashakkur!',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect('Home')  # 🔹 Ro‘yxatdan o‘tganidan keyin `home` ga yo‘naltirish

    return render(request, 'auth/register.html')


def login_user(request):
    if request.user.is_authenticated:  # 🔹 Login bo'lgan foydalanuvchilar kira olmasin
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')  # 🔹 Tizimga kirgandan keyin `home` ga yo‘naltirish
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')  # 🔹 Logout qilgandan keyin login sahifasiga yo‘naltirish


import random
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

User = get_user_model()

# 📌 Kodlarni vaqtincha saqlash uchun dictionary
RESET_CODES = {}

# 🔹 Forgot Password - Email Kiritish Sahifasi
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # 1️⃣ **Email mavjudligini tekshirish**
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "This email is not registered!")
            return redirect('forgot_password')

        # 2️⃣ **Tasdiqlash kodi yaratish va email jo‘natish**
        reset_code = str(random.randint(100000, 999999))  # 6 xonali kod
        RESET_CODES[email] = reset_code  # Kodni saqlash

        send_mail(
            'Password Reset Code',
            f'Your password reset code is: {reset_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # 3️⃣ **Tasdiqlash kodini kiritish sahifasiga yo‘naltirish**
        return redirect(f'/auth/verify-reset-code/?email={email}')

    return render(request, 'auth/forgot.html')


# 🔹 Verify Reset Code - Kiritilgan Kodni Tekshirish
def verify_reset_code(request):
    email = request.GET.get('email')

    if request.method == 'POST':
        entered_code = request.POST.get('code')

        # **Kodni tekshirish**
        if email in RESET_CODES and RESET_CODES[email] == entered_code:
            return redirect(f'/auth/reset-password-done/?email={email}')
        else:
            messages.error(request, "Invalid code!")
            return redirect(f'/auth/verify-reset-code/?email={email}')

    return render(request, 'auth/code.html', {"email": email})


# 🔹 Reset Password - Yangi Parolni Kiritish
def reset_password_done(request):
    email = request.GET.get('email')

    if request.method == 'POST':
        new_password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect(f'/auth/reset-password-done/?email={email}')

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password has been reset! You can now log in.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Something went wrong!")
            return redirect('forgot_password')

    return render(request, 'auth/password_reset_done.html', {"email": email})
