from django import forms
# from datetimepicker.widgets import DateTimePicker


from .models import Project,User,Timesheet

class timeSheetForm(forms.Form):
    # fields=['project','user','task_title','task_description','priority','starting_time','ending_time']
    PRIORITY_STATUS = [
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    ]
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="(No Project)")
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="(No User)")
    task_title = forms.CharField(max_length=250)
    task_description = forms.CharField(widget=forms.TextInput({}))
    priority = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=PRIORITY_STATUS),
    )
    starting_time = forms.DateTimeField()
    ending_time = forms.DateTimeField()