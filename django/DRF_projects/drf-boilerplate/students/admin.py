from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "birthday",
        "gender",
        "gpa",
        "module_id",
        "created_at",
        "updated_at",
    ]
