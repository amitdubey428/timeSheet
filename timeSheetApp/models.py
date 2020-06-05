from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    RESPONSIBILITY = (
        ('PM','Project Manager'),
        ('SM','Scheduling Manager'),
        ('PC','Project Collaborator'),
    )
    roles = models.CharField(max_length=2, choices=RESPONSIBILITY)

    def __str__(self):
        return str(self.first_name)+" "+str(self.last_name)

class AdminRole(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    
    def __str__(self):
        return str(self.first_name,self.last_name)


class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=250)
    user= models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    STATUS = (
        ('S','Started'),
        ('O','On going'),
        ('C','Completed'),
    )
    project_status = models.CharField(max_length=1, choices=STATUS, null=False)
    
    def __str__(self):
        return str(self.project_title)

<<<<<<< HEAD

=======
>>>>>>> 5dada286eb935671bb9887faf57a6bb50a29f11a
class Timesheet(models.Model):
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    task_title = models.CharField(max_length=250)
    task_description = models.TextField(null=True)
    PRIORITY_STATUS = (
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_STATUS)
    starting_time = models.DateTimeField(auto_now_add=False)
    ending_time = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return str(self.task_title)

