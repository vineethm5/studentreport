from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(student)
admin.site.register(StudendId)
admin.site.register(Department)
admin.site.register(subject)


class dis(admin.ModelAdmin):
    list_display=['student','subject','marks']


admin.site.register(subjectmarks,dis)