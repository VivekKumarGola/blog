from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('user_login')
        return render(request,'login.html')



def logout_user(request):
    logout(request)
    return redirect("user_login")


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            user = User.objects.create_user(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
                username=request.POST.get('email')
            )
            user.save()
            return redirect('user_login')
        return render(request,'signup.html')

