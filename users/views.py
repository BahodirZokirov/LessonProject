from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    else:
        context = {
            "form": form
        }
        return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect("home")
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
