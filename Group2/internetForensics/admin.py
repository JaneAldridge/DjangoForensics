from django.contrib import admin
from internetForensics.models import userProfile #IMPORTING USERPROFILE MODEL
from django.contrib.auth.models import User #IMPORTING USER MODEL
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AccountInline(admin.StackedInline): # AN ESXITING CLASS TO INHERIT FROM SO AS TO HAVE YOUR OWN FIELDS IN USER MODEL (FROM DJANGO DOCUMENTATION)
    model = userProfile
    can_delete = False #AVOIDS DELETION OF USERPROFILE IF THE USER IS NOT DELETED
    verbose_name_plural = 'userProfile'

 #TO REGISTER THE USERPROFILE MODEL TO THE USER MODEL
class customizedUserAdmin (UserAdmin):
    inlines = (AccountInline,)



admin.site.unregister(User)
admin.site.register(User, customizedUserAdmin)