#DJANGO IMPORTS

from django.contrib import admin
from django.conf import settings
from django.shortcuts import render, redirect #to allow redirection from one page to another pages
from django.http import HttpResponse #FOR HTTP RESPONSE
from django.contrib.auth.models import User #FOR IMPORTING USERS DATABASE
from django.contrib.auth import authenticate, login, logout #FOR AUTH AND LOGOUT
from django.contrib.auth.models import Group
from django.contrib import messages #FOR ERROR AND INFORMATION/STATUS MESSAGES 
from django.contrib.auth.decorators import login_required #FOR ENABLING VIEW RESTRICTIONS UNTIL LOGGED IN 
from .decorators import unauthenticated_user, allowed_users, admin_only #FOR IMPORTING THE USER ACCESS CONTROL DECORATORS

# Create your views here.

 # LOGIN  REQUEST, AUTHENTICATION AND RESTRICTION TO AN ALREADY AUTHENTICATED USER

@unauthenticated_user # only accessed to unauthenticated users and restriction put on validated users who try to go back to login page via the URL 
def Login(request):

    if request.method == 'POST': #authentication
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

@login_required(login_url='login')   # RESTRICTION ON UNAUTHENTICATED USERS AND DERIVED FROM 'IMPORT LOGIN_REQUIRED'
@allowed_users(allowed_roles=['admin','managers','senior_security_analysts','junior_security_analyst','police_officers']) # ACCESS CONTROL AS PER THE USER ROLES 
def mainpage(request):
    return render(request, 'internetForensics/mainpage.html')

@login_required(login_url='login')    # RESTRICTION ON UNAUTHENTICATED USERS AND DERIVED FROM 'IMPORT LOGIN_REQUIRED'
@allowed_users(allowed_roles=['admin','managers','senior_security_analysts','junior_security_analyst','police_officers']) # ACCESS CONTROL AS PER THE USER ROLES 
def reports(request): #to view report management page
    return render(request, 'internetForensics/reports.html')

@login_required(login_url='login')   # RESTRICTION ON UNAUTHENTICATED USERS AND DERIVED FROM 'IMPORT LOGIN_REQUIRED'
@allowed_users(allowed_roles=['admin','managers','senior_security_analysts','junior_security_analyst','police_officers']) # ACCESS CONTROL AS PER THE USER ROLES 
def criminalActivity(request): #to view search and locate criminal activities page
    return render(request, 'internetForensics/criminalactivity.html')

@login_required(login_url='login')    # RESTRICTION ON UNAUTHENTICATED USERS AND DERIVED FROM 'IMPORT LOGIN_REQUIRED'
@allowed_users(allowed_roles=['admin','managers','senior_security_analysts']) # ACCESS CONTROL AS PER THE USER ROLES 
def audits(request): #to view audits page
    return render(request, 'internetForensics/audits.html')   

@login_required(login_url='login')    # RESTRICTION ON UNAUTHENTICATED USERS AND DERIVED FROM 'IMPORT LOGIN_REQUIRED'
@allowed_users(allowed_roles=['admin','managers','senior_security_analysts','junior_security_analyst','police_officers']) # ACCESS CONTROL AS PER THE USER ROLES 
def cases(request): #to view cases page
    return render(request, 'internetForensics/cases.html')

