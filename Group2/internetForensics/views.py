#DJANGO IMPORTS

from django.contrib import admin
from django.conf import settings
from django.shortcuts import render, redirect #to allow redirection from one page to another pages
from django.http import HttpResponse #FOR HTTP RESPONSE
from django.contrib.auth.models import User #FOR IMPORTING USERS DATABASE
from django.contrib.auth import authenticate, login, logout #FOR AUTH AND LOGOUT

from django.contrib import messages #FOR ERROR AND INFORMATION/STATUS MESSAGES 
from django.contrib.auth.decorators import login_required #FOR ENABLING VIEW RESTRICTIONS UNTIL LOGGED IN 


# Create your views here.

 # LOGIN  REQUEST, AUTHENTICATION AND RESTRICTION TO AN ALREADY AUTHENTICATED USER

def Login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('mainpage')
        
        else:
            messages.info(request, 'Invalid Username or Password')
    
    return render(request, 'internetForensics/login.html')


# LOG OUT REQUEST
def logoutUser(request):
    logout(request)
    return redirect('login')



# VIEW REQUESTS FOR THE REST OF THE PAGES AND ACCESS RESTRICTIONS

@login_required(login_url='login')   # RESTRICTION PUT FROM 'IMPORT LOGIN_REQUIRED'
def mainpage(request):
    return render(request, 'internetForensics/mainpage.html')

@login_required(login_url='login')   # RESTRICTION PUT FROM 'IMPORT LOGIN_REQUIRED'
def reports(request): #to view report management page
    return render(request, 'internetForensics/reports.html')

@login_required(login_url='login')   # RESTRICTION PUT FROM 'IMPORT LOGIN_REQUIRED'
def criminalActivity(request): #to view search and locate criminal activities page
    return render(request, 'internetForensics/criminalactivity.html')

@login_required(login_url='login')   # RESTRICTION PUT FROM 'IMPORT LOGIN_REQUIRED'
def audits(request): #to view audits page
    return render(request, 'internetForensics/audits.html')   

@login_required(login_url='login')   # RESTRICTION PUT FROM 'IMPORT LOGIN_REQUIRED'
def cases(request): #to view cases page
    return render(request, 'internetForensics/cases.html')

