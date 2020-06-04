from django.contrib import admin

# Register your models here.
from .models import User, Project, Timesheet, Add_Member, AdminRole

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Add_Member)
admin.site.register(Timesheet)
admin.site.register(AdminRole)
