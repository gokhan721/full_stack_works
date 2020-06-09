from django.contrib import admin
from cbv_app.models import *


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "principal", "location")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "school")


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
