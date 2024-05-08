from django.contrib import admin
from .models import Module


# Register your models here.
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "code",
        "created_at",
        "updated_at",
    ]
