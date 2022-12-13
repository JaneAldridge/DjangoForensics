from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout #FOR AUTH

# Create your views here.

 # LOGIN  REQUEST AND AUTH 

def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
   
    if user is not None:
        login(request, user)
        return redirect('mainpage')
    else:
        messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, 'internetForensics/index.html', context)


# LOG OUT
def logoutUser(request):
    return redirect('index')

# REQUESTS FOR THE REST OF THE PAGES 
def mainpage(request):
    return render(request, 'internetForensics/mainpage.html')
    
def reports(request): #report management
    return render(request, 'internetForensics/reports.html')

def criminalActivity(request): #search and locate criminal activities
    return render(request, 'internetForensics/criminalactivity.html')

def audits(request): #manage audits
    return render(request, 'internetForensics/audits.html')   

def cases(request): #manage cases
    return render(request, 'internetForensics/cases.html')

