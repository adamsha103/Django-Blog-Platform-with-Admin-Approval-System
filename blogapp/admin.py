from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    actions = ['make_published']

    @admin.action(description='Mark selected posts as Published')
    def make_published(self, request, queryset):
        queryset.update(status='Published')
