from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    post_list = ['title','thumbnail','description']
    list_display = post_list
    search_fields = post_list
    list_filter = post_list

admin.site.register(Category)
admin.site.register(UserAbout)
admin.site.register(Post,PostAdmin)
admin.site.register(Assets)
admin.site.register(Rating)
admin.site.register(Comment)

