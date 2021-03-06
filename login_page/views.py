from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

"""
Referensi : 
- https://www.ordinarycoders.com/blog/article/django-user-register-login-logout
- https://www.ordinarycoders.com/blog/article/django-messages-framework
- http://www.learningaboutelectronics.com/Articles/How-to-check-whether-a-username-already-exists-in-Django.php
"""

# Create your views here.
def register_user(request):
    if (request.method == 'POST'):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_pass = form.cleaned_data.get('confirm_password')
            if (password == confirm_pass):
                try:
                #Cek jika username atau email sudah terdaftar
                    user = User.objects.get(username=username)
                    user_email = User.objects.get(email=email)
                    context = {'form' : form}
                    messages.error(request, 'Email or username has already been taken.')
                    return render(request, 'login_page/register.html', context)
                except (User.DoesNotExist):
                #Jika username atau email belum terdaftar
                    user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    form.save()
                    context = {'form' : form}
                    messages.success(request, 'Registration successful!')
                    return HttpResponseRedirect('login')

            context = {'form' : form}
            messages.error(request, "Passwords entered don't match")
            return render(request, 'login_page/register.html', context)

    form = RegisterForm()
    context = {'form' : form}
    return render(request, 'login_page/register.html', context)

def login_user(request):
    redirect_to = request.GET.get('next', 'home-page')
    if (request.method == 'POST'):
        form = AuthenticationForm(request, request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                messages.success(request, 'Login successful!')
                messages.info(request, f"Logged in as {username}.")
                return HttpResponseRedirect(redirect_to=redirect_to)
        
        messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'login_page/login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'Successfully logged out')
    return HttpResponseRedirect('home-page')

def home_page(request):
    return render(request, 'home_page/home.html')

@csrf_exempt
def register_flutter(request):
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    username = data['username']
    password = data['password']
    confirm_pass = data['confirm_password']
    print(username)
    print(password)
    print(confirm_pass)

    if (password == confirm_pass):
        try:
        #Cek jika username atau email sudah terdaftar
            user = User.objects.get(username=username)
            print(user)
            user_email = User.objects.get(email=email)
            return JsonResponse({'status':'register gagal'})
        except (User.DoesNotExist):
        #Jika username atau email belum terdaftar
            user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            return JsonResponse({'status':'register berhasil', 'username':username, 'password':password})

@csrf_exempt
def login_flutter(request):
    data = json.loads(request.body)
    print(request.method)
    username = data['username']
    password = data['password']
    print(username)
    print(password)

    user = authenticate(username=username, password=password)
    print(user)
    if (user is not None):
        return JsonResponse({'status':'logged in', 'username':username})
    else:
        return JsonResponse({'status':'failed'})