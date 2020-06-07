from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import SplitDateTimeField

from .models import Project,User,Timesheet

class timeSheetForm(forms.Form):
    # fields=['project','user','task_title','task_description','priority','starting_time','ending_time']
    PRIORITY_STATUS = [
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    ]
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(No User)")
    task_title = forms.CharField(max_length=250)
    task_description = forms.CharField(widget=forms.TextInput({}))
    priority = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=PRIORITY_STATUS),
    )
    starting_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    ending_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    