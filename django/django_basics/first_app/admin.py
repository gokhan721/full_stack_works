from django.contrib import admin
from first_app.models import *

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ("top_name",)


class WebpageAdmin(admin.ModelAdmin):
    list_display = ("topic", "name", "url")

class AccessRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "date")


admin.site.register(Topic, TopicAdmin)
admin.site.register(Webpage, WebpageAdmin)
admin.site.register(AccessRecord, AccessRecordAdmin)
