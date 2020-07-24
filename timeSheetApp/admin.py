from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Profile, Project, Timesheet


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Timesheet)
