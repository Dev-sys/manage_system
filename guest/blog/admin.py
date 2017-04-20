from django.contrib import admin
from blog.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'create_time')

admin.site.register(Blog, BlogAdmin)