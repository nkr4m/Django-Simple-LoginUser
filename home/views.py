from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return render(request, "login.html")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        #check if user has logged in with correct cred
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return render(request, "login.html")