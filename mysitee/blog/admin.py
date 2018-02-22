from django.contrib import admin
from blog.models import Post, Category
# Register your models here.
class Padmin(admin.ModelAdmin):
	list_filter = ['posttime']
	search_fields = ['title', 'text']
	list_display = ['title','category']

admin.site.register(Post,Padmin)
admin.site.register(Category)