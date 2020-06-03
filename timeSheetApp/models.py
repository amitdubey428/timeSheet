from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_id = models.EmailField(unique=True)
    # password = models.Char        integrate it in form
    phone_no = models.CharField(max_length=12)
    RESPONSIBILITY = (
        ('PM','Project Manager'),
        ('SM','Scheduling Manager'),
        ('PC','Project Collaborator'),
    )
    roles = models.CharField(max_length=2, choices=RESPONSIBILITY)
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()

    def __str__(self):
        return str(self.first_name)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return str(self.project_title)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    task_title = models.CharField(max_length=250)
    description = models.TextField()
    STATUS = (
        ('S','Started'),
        ('O','On going'),
        ('C','Completed'),
    )
    task_status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return str(self.task_title)

