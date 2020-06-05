from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'timeSheetApp/index.html')

def memberDash(request):
    return render(request,'timeSheetApp/dashboard.html')

def users(request):
    return render(request,'timeSheetApp/user.html')