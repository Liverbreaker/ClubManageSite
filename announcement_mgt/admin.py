from django.contrib import admin
from announcement_mgt import models

# Register your models here.
@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Announcement._meta.get_fields()]
