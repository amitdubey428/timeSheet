from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import User, Project, Timesheet, AdminRole
=======
from .models import User, Project, Timesheet , AdminRole
>>>>>>> 5dada286eb935671bb9887faf57a6bb50a29f11a

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Timesheet)
admin.site.register(AdminRole)
