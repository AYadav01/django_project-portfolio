from django.shortcuts import render

# Create your views here.
def allprojects(request):
	return render(request, 'projects/project.html')