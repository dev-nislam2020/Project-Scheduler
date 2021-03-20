from django.contrib import admin

from pro_sch.models import (Feature, Framework, Interface, Language, Logical,
                            Project, Stage, Status)

# Register your models here.
admin.site.register(Feature)
admin.site.register(Framework)
admin.site.register(Interface)
admin.site.register(Language)
admin.site.register(Logical)
admin.site.register(Project)
admin.site.register(Stage)
admin.site.register(Status)
