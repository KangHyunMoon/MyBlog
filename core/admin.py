from django.contrib import admin

from django.contrib import admin
from core.models import Post

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)

# Register your models here.
