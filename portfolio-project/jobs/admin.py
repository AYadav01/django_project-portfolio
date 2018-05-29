from django.contrib import admin

# Register your models here to show up in the admin page
from .models import Job

admin.site.register(Job)
