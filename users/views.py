from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = email  # обязательное поле
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        country = request.POST.get("country")

        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            phone_number=phone_number,
            country=country
        )

        login(request, user)
        return redirect('index')  # главная после регистрации

    return render(request, "users/register.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
