from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'badpress/home.html')


def stateresults(request):
	return render(request, 'badpress/stateresults.html')


def candidate(request):
	return render(request, 'badpress/candidate.html')


def issue(request):
	return render(request, 'badpress/issue.html')



def article(request):
	return render(request, 'badpress/article.html')
	


def about(request):
	return render(request, 'badpress/about.html')

