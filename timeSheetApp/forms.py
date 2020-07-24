from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import SplitDateTimeField
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Project, Timesheet, Profile

class timeSheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields="__all__"
    # def __init__(self,*args,**kwargs):
    #     super(timeSheetForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].initial = self.data
    #     print(self.fields['user'])
    # fields=['project','user','task_title','task_description','priority','starti
    # ng_time','ending_time']
    PRIORITY_STATUS = [
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    ]
    
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput())
#     user = forms.ModelChoiceField(queryset=User.objects.all())
    task_title = forms.CharField(max_length=250)
    task_description = forms.CharField(widget=forms.TextInput({}))
    priority = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=PRIORITY_STATUS),
    )
    starting_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    ending_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())


    
