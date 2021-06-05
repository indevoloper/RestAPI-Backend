from django.contrib import admin
from .models import app

class appAdmin(admin.ModelAdmin):
    list_display = ('username', 'lastname', 'age','weight','gender')

# Register your models here.

admin.site.register(app, appAdmin)
