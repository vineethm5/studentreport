from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(student)
admin.site.register(StudendId)
admin.site.register(Department)
admin.site.register(subject)
admin.site.register(subjectmarks)

class dis(admin.ModelAdmin):
    model=subjectmarks
    list_display=['subject','marks']