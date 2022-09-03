from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *
from django.contrib import messages


def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = UserAbout.objects.get_or_create(user=request.user)
            
            if request.POST.get("profile") != '':
                request.user.about.profile_pic = request.FILES['profile']
                request.user.first_name = request.POST.get("first_name")
                request.user.last_name = request.POST.get("last_name")
                request.email = request.POST.get("email")
                request.user.about.address  = request.POST.get("address")
                request.user.about.phone = request.POST.get("phone")
                request.user.about.save()
                request.user.save()
            else:
                request.user.first_name = request.POST.get("first_name")
                request.user.last_name = request.POST.get("last_name")
                request.user.email = request.POST.get("email")
                request.user.about.address  = request.POST.get("address")
                request.user.about.phone = request.POST.get("phone")
                request.user.about.save()
                request.user.save()
            return redirect('dashboard')
        else:
            return render(request,'index.html')
    else:
        return redirect("user_login")

def post(request):
    if request.user.is_authenticated:
        return render(request,'posts.html')
    else:
        return redirect("user_login")


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('id')!='':
                post = request.user.post.get(
                    pk=request.POST.get('id')
                )
                if request.POST.get("thumbnail"):
                    post.thumbnail = request.FILES["thumbnail"]
                    post.title=request.POST.get("title")
                    post.description=request.POST.get("desc")
                    post.save()
                else:
                    post.title=request.POST.get("title")
                    post.description=request.POST.get("desc")
                    post.save()
                return redirect("post")
            else:
                print(request.POST.get("image"))
                if request.POST.get("image"):
                    post = Post(
                        user=request.user,
                        thumbnail=request.FILES["image"],
                        category=Category.objects.get(id=request.POST.get("category")),
                        title=request.POST.get("title"),
                        description=request.POST.get("desc")
                    )
                    post.save()
                else:
                    post = Post(
                        user=request.user,
                        category=Category.objects.get(id=request.POST.get("category")),
                        title=request.POST.get("title"),
                        description=request.POST.get("desc")
                    )
                    post.save()
                messages.success(request,"Post Save Successfully")
                return redirect("add_post")
        cat = Category.objects.all()
        context = {
            "cat":cat
        }
        return render(request,'add_post.html',context)
    else:
        return redirect("user_login")


def update_post(request,id):
    if request.user.is_authenticated:

        post = Post.objects.get(pk=id)
        print(post.title)
        cat = Category.objects.all()
        context = {
            "cat":cat,
            "post":post
        }
        return render(request,'add_post.html',context)
    else:
        return redirect("user_login")

def del_post(request,id):
    if request.user.is_authenticated:
        post = request.user.post.get(id=id)
        post.delete()
        return redirect("post")
    else:
        return redirect("user_login")
