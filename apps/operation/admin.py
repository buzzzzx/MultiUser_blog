from django.contrib import admin

from .models import PostComment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'post', 'active', 'created')
    list_filter = ('user', 'post', 'active')
    search_fields = ('body', 'active')
    raw_id_fields = ('user',)
    date_hierarchy = 'created'
    ordering = ['active', 'created']


admin.site.register(PostComment, CommentAdmin)
