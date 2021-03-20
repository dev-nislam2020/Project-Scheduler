from django.contrib import admin

from pro_sch.models import Project, Stage, Status

# Register your models here.
admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Stage)
