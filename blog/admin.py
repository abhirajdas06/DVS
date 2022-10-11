from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
from django.contrib import admin
from .models import Post, Category  

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug')
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Category, CategoryAdmin)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug',)
#     search_fields = ['title', 'body']
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)


admin.site.register((Post, Category, Comment))
# admin.site.register(Category)
# admin.site.register(Comment)
