from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blogId):
	detailblog = get_object_or_404(Blog, pk=blogId)
	return render(request, 'blog/detail.html', {'blog':detailblog})

def search(request):
	title_search = request.GET['title']
	blogs = Blog.objects.filter(title__icontains=title_search)
	if blogs:
		return render(request, 'blog/allblogs.html', {'blogs':blogs})
	else:
		error = "'{0}' is not a valid blog title".format(title_search)
		return render(request, 'blog/allblogs.html', {'error':error})