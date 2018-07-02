from django.shortcuts import render

# Create your views here.
def allprojects(request):
	return render(request, 'projects/project.html')

def wordcounter(request):
	return render(request, 'projects/first_project.html')

def count(request):
	import operator
	fulltext = request.GET['fulltext']
	wordList = fulltext.split()
	counter = 1
	myDict = {}
	for word in wordList:
		if word.lower() not in myDict:
			myDict[word.lower()] = counter
		else:
			myDict[word.lower()] = myDict.get(word, "")+1

	sortedWords = sorted(myDict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'projects/count.html', {'fulltext': fulltext, 'count': len(wordList),
		'myDict':sortedWords})

def htmlTag(request):
	return render(request, 'projects/second_project.html')

def htmlTagFinder(request):
	import urllib.request
	import re
	#get the contents first
	urls = request.GET['urls']
	if urls.startswith('https://'):
		pass
	else:
		urls = 'https://'+str(urls)
	#extracting the html contents
	with urllib.request.urlopen(urls) as file:
		contents = file.read()
	pattern = re.compile(r'<[a-zA-Z0-9\s=""\.-]+>')
	matches = pattern.finditer(str(contents))
	array = [] #for storing tags
	for match in matches:
		index = match.span()
		array.append(str(contents)[index[0]:index[1]])
	#return the template and tags
	return render(request, 'projects/tagFinder.html', {'array':array,'url':urls})

