from django.contrib import admin
from .models import Club
from users_mgt.admin import MemberInline

# Register your models here.
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'is_activate', 'office', 'teacher',)
    inlines = [MemberInline]
