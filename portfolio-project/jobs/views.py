from django.shortcuts import render
from django.http import HttpResponse

#to access items to database
from .models import Job

# Create your views here.
def home(request):
	#grap all job objects from database and convert them into python object
	jobs = Job.objects #this will be the dictionary

	#get the jobs here and send them to here
	return render(request, 'jobs/home.html', {'jobs': jobs})