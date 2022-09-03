from django.shortcuts import render
from blog.models import *
from .models import AboutU
def main(request):
    about = AboutU.objects.all().first()
    category = Category.objects.all()
    post = Rating.objects.all()
    all_post = Post.objects.all().order_by("date")[:4]
    context = {
        'about':about,
        'category':category,
        'post':post,
        'all_post':all_post
    }
    return render(request,'home.html',context)


def post_details(request,id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request,'view-post.html',context)


def get_post_by_category(request,id):
    about = AboutU.objects.all().first()
    category = Category.objects.all()
    post = Rating.objects.all()
    all_post = Post.objects.filter(category__id=id)
    context = {
        'about':about,
        'category':category,
        'post':post,
        'all_post':all_post
    }
    return render(request,'home.html',context)
