from django.shortcuts import render
from django.http import Http404


from .models import Timesheet,Project,User
from .forms import timeSheetForm

# Create your views here.
def index(request):
    return render(request,'timeSheetApp/index.html')

def memberDash(request):
    form = timeSheetForm()
    timeSheetData = Timesheet.objects.filter(user=1)
    context={
        'form':form,
        'timeSheetData':timeSheetData
    }
    if request.method == 'POST':
        newTimeSheet = Timesheet()
        newTimeSheet.project = Project.objects.get(pk=request.POST["project"])
        newTimeSheet.user =  User.objects.get(pk=request.POST["user"])
        newTimeSheet.task_title = request.POST["task_title"]
        newTimeSheet.task_description = request.POST["task_description"]
        newTimeSheet.priority = request.POST["priority"]
        newTimeSheet.starting_time = request.POST["starting_time"]
        newTimeSheet.ending_time = request.POST["ending_time"]

        newTimeSheet.save()
       
        return render(request,'timeSheetApp/dashboard.html',context)
    else:
        
        return render(request,'timeSheetApp/dashboard.html',context)

def users(request):
    return render(request,'timeSheetApp/user.html')