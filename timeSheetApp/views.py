from django.shortcuts import render,HttpResponse,redirect
from django.http import Http404,HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.core.exceptions import PermissionDenied


from .models import Timesheet,Project,Profile
from .forms import timeSheetForm

# Create your views here.
def index(request):
    if request.session.has_key('username'):
        return redirect("empDashboard")
    else:
        return render(request,'timeSheetApp/index.html')

def contact(request):
    if request.session.has_key('username'):
        return redirect("empDashboard")
    else:
        return render(request,'timeSheetApp/contact.html')

def loginEmp(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
        if(user.groups.filter(name='Employee').exists()):
            request.session['username'] = username
            return redirect("/memberDashboard")
        else:
            raise PermissionDenied()
    else:
        return redirect("home")

def loginAdmin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_staff:

            request.session['username'] = username
            return redirect("/admin")
        else:
            raise PermissionDenied()
        
    else:
        return redirect("home")
    
    
       

# @login_required
def memberDash(request):
    if request.user.is_authenticated:
        form = timeSheetForm(initial={'user': request.user})
        timeSheetData = Timesheet.objects.filter(user=request.user)
        context={
            'form':form,
            'timeSheetData':timeSheetData
        }
        if request.method == 'POST':
            print(request.POST)
            newTimeSheet = timeSheetForm(request.POST)

            if newTimeSheet.is_valid():
            # newTimeSheet.project = Project.objects.get(pk=request.POST["project"])
            # newTimeSheet.user =  User.objects.get(pk=request.POST["user"])
            # newTimeSheet.task_title = request.POST["task_title"]
            # newTimeSheet.task_description = request.POST["task_description"]
            # newTimeSheet.priority = request.POST["priority"]
            # newTimeSheet.starting_time = request.POST["starting_time"]
            # newTimeSheet.ending_time = request.POST["ending_time"]

                newTimeSheet.save()
        
                return render(request,'timeSheetApp/dashboard.html',context)
        else:
            return render(request,'timeSheetApp/dashboard.html',context)
    else:  
        return redirect("home")

def summary(request):
    if request.user.is_authenticated:
        countUser=User.objects.all().count()
        countSheet=Timesheet.objects.all().count()
        countProject=Project.objects.all().count()
        labelC=[]
        dataC=[]
        labelP=[]
        dataP=[]
        Projects=[]
        queryset = Timesheet.objects.filter(user=request.user)
        projectSet = Timesheet.objects.all()
        for sheet in queryset:
            duration=sheet.ending_time-sheet.starting_time
            labelC.append(sheet.task_title)
            dataC.append(int(duration.total_seconds())//3600)
            
        for sheet in projectSet:
            Projects.append(sheet.project.project_title)
        freq = {} 
        for items in Projects:
            freq[items] = Projects.count(items)
        items = freq.items() 
        for item in items:
            labelP.append(item[0]), dataP.append(item[1])

        # print(labelP,dataP)
        context = {
            'countP':countProject,
            'countT':countSheet,
            'countU':countUser,
            'labelC':labelC,
            'dataC':dataC,
            'labelP':labelP,
            'dataP':dataP
        }
        # print(context)
        return render(request,'timeSheetApp/summary.html',context)
    else:
        return redirect("home")

# @login_required
def users(request):
    if request.user.is_authenticated:
        profile=Profile.objects.filter(user=request.user)
        # print(profile.roles)
        context={
            'profile':profile
        }
        # print(context)
        return render(request,'timeSheetApp/user.html',context)
    else:  
        return redirect("home")


def logoutUser(request):
    if request.session.has_key('username'):
        request.session.flush()
        logout(request)
        return redirect("home")