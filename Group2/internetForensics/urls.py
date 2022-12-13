from django.urls import path
from . import views #importing from views.py file 

#importing the url path from views.py file 
urlpatterns = [

    path('', views.index, name="index"),
    path('index/',views.index, name="index"),
    path('mainpage/',views.mainpage, name="mainpage"),
    path('reports/',views.reports, name="reports"),
    path('criminalactivity/',views.criminalActivity, name="criminalactivity"),
    path('audits/',views.audits, name="audits"),
    path('cases/',views.cases, name="cases"),
    
]
