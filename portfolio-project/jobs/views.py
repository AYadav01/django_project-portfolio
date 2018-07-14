from django.shortcuts import render, redirect

#to access items to database
from .models import Job

#import Form
from . import forms

#import for emails
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	#grap all job objects from database and convert them into python object
	jobs = Job.objects #this will be the dictionary

	#get the jobs here and send them to here
	return render(request, 'jobs/home.html', {'jobs': jobs})

def suggest_me(request):

	#make a blank form instance
	form = forms.SuggestionForm()

	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		#check if the fields are cleaned 
		if form.is_valid():

			subject = "Thank you for your suggestion"
			message = "I appreciate your time and effort in sending me your suggestion. I will get back to you ASAP :-)"
			from_email = settings.EMAIL_HOST_USER

			#sending it to myself and the email that the user puts in
			to_email = [form.cleaned_data['email']]

			send_mail(subject, message, from_email, to_email, fail_silently=True)
			messages.success(request, messages.SUCCESS, 'Thank you for your suggestion!')
			return render(request, 'jobs/thank_you.html', {'name':form.cleaned_data['name']})

	return render(request, 'jobs/suggest_me.html', {'form':form})