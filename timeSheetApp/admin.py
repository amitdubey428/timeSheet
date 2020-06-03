from django.contrib import admin

# Register your models here.
from .models import User, Project, Timesheet, Assigned_Project_Member

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Assigned_Project_Member)
admin.site.register(Timesheet)
