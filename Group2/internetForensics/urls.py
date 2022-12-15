from django.urls import path #IMPORTING PATH TO CREATE PATHS TO HTML PAGES
from django.contrib import admin
from . import views #Importing from views.py file 
from internetForensics.views import login
from .views import login

#importing the url path from views.py file 

urlpatterns = [



    path('', views.Login, name="login"),
    path('login/',views.Login, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('mainpage/',views.mainpage, name="mainpage"),
    path('reports/',views.reports, name="reports"),
    path('criminalactivity/',views.criminalActivity, name="criminalactivity"),
    path('audits/',views.audits, name="audits"),
    path('cases/',views.cases, name="cases"),

]
