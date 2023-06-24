from django.contrib import admin
from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in File._meta.get_fields()]