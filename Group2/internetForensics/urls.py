#DJANGO IMPORTS

from django.urls import path #IMPORTING PATH TO CREATE PATHS TO HTML PAGES
from django.contrib import admin
from . import views #Importing from views.py file 
from internetForensics.views import login
from .views import login
from django.contrib.auth import views as auth_views



#importing the url path from views.py file 

urlpatterns = [
    path('', views.Login, name="login"),
    path('login/',views.Login, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('mainpage/',views.mainpage, name="mainpage"),
    path('manage_reports/',views.manage_reports, name="manage_reports"),
    path('create_reports/',views.create_reports, name="create_reports"),
    path('criminalactivity/',views.criminalActivity, name="criminalactivity"),
    path('audits/',views.audits, name="audits"),
    path('cases/',views.cases, name="cases"),
    path('userslogs/',views.userslogs, name="userslogs"),
    path('changepassword/', auth_views.PasswordChangeView.as_view(), name="changepassword"),


]
