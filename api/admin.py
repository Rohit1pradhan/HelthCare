from django.contrib import admin

from api.models import User, HelthCare


# Register your models here.
@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','age','mobile','password']
@admin.register(HelthCare)
class helthAdmin(admin.ModelAdmin):
    list_display = ['id','user','madicine','timing']

