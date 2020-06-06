from django.shortcuts import render
from django.http import Http404


from .forms import timeSheetForm

# Create your views here.
def index(request):
    return render(request,'timeSheetApp/index.html')

def memberDash(request):
    if request.method == 'POST':
        form = timeSheetForm(request.POST)
        if form.is_valid():
            return render(request,'timeSheetApp/dashboard.html')
    else:
        form = timeSheetForm()
    context={
        'form':form,
    }
    return render(request,'timeSheetApp/dashboard.html',context)

def users(request):
    return render(request,'timeSheetApp/user.html')