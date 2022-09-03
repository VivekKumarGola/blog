from distutils.command.upload import upload
from turtle import goto
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class UserAbout(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='about')
    profile_pic = models.ImageField(upload_to='profile_pics/')
    phone = models.CharField(max_length=12)
    address = models.TextField()
    description = models.TextField()
    date_of_birth = models.DateTimeField(null=True,blank=True)
    def __str__(self) -> str:
        return self.user.first_name


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="post/image/",blank=True,null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    snippet = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.user.first_name + " " +self.user.last_name 

class Assets(models.Model):
    post = models.ManyToManyField(Post,blank=True,null=True)
    user = models.ManyToManyField(User,blank=True,null=True)
    def __str__(self) -> str:
        return self.post.title

class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="rating")
    bad = models.BooleanField(default=False)
    average = models.BooleanField(default=False)
    good  = models.BooleanField(default=False)
    vgood  = models.BooleanField(default=False)
    excellent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self) -> str:
        return self.post.title
