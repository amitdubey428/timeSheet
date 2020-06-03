from django.contrib import admin

# Register your models here.
from .models import User, Project, Timesheet

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Timesheet)
