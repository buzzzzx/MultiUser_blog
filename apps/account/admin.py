from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'is_active', 'is_staff')
    list_filter = ('gender', 'is_active', 'is_staff')
    search_fields = ('username', 'gender', 'email', 'is_active')


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
