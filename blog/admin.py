from django.contrib import admin
from .models import Post, Category, Tag, User


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'author', 'publish_date', 'for_logged_users_only')
    prepopulated_fields = {'slug': ['title']}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ['name']}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ['name']}


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)