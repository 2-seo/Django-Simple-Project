from django.contrib import admin
from .models import Myuser

class MyuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Myuser, MyuserAdmin)