from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            return redirect('register')
    else:
        form = CustomUserCreationForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "users/login.html", context)

