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
