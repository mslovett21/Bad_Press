from django.shortcuts import render, HttpResponse, Http404, redirect
from django.views import generic
from .models import Source, State, Issue, Article, Candidate, Popularity, Cloud
from badpress.forms import HomeForm
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Render the HTML template index.html with the data in the context variable
	queryset = Candidate.objects.all()



	context = {
		"candidate_list": queryset,
		#"text": text,
	}

	return render(
		request,
		'badpress/home.html',
		context
	)


def state(request, slug):
	try:
		state_name=State.objects.get(name=slug)
	except State.DoesNotExist:
		return redirect('not_found_state')

	try:
		candidates=Candidate.objects.filter(state=state_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")
	print(state_name.id)

	args={'candidates': candidates, 'state': state_name,}
	return render(request, 'badpress/candidate_list.html', args)

def candidate(request, last_name):
	try:
		candidate=Candidate.objects.get(last_name=last_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	candidate_id=candidate.id
	candidate_last=candidate.last_name
	state=candidate.state
	number_candidates=Candidate.objects.count()


	popularity= Popularity.objects.get(last_name=candidate_last)
	cloud = Cloud.objects.get(last_name=candidate_last)
	articles = Article.objects.filter(candidate=candidate).order_by('date')[:6]
	print(articles)

	state_image=""

	date="6th May 2018"

	args={'candidate':candidate,'state': state, 'state_image' : state_image, "popularity": popularity,
	 "number_candidates": number_candidates, 'cloud' : cloud, 'articles':articles}
	return render(request, 'badpress/candidate.html', args)


def issue(request, id, last_name):
	try:
		candidateS=Candidate.objects.get(last_name=last_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	try:
		if int(id) <7:
			issueS = Issue.objects.get(issue_id=id)
			article = Article.objects.filter(candidate=candidateS).filter(issue=issueS)
			issue = Issue.objects.get(issue_id=id)
		else:
			article = Article.objects.filter(candidate=candidateS)
			issue = Issue.objects.get(issue_id=6)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")


	try:

		source= Source.objects.all()
	except Source.DoesNotExist:
		raise Http404("Source does not exist")


	number=len(article)
	args={	"articles": article,
			"issue": issue,
			"source": source,
			"candidate": candidate,
			"number": number
	}
	return render(request, 'badpress/issue.html',args)


def article(request, id):
	try:
		article = Article.objects.get(article_id=id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	try:
		candidate_id=Candidate.objects.get(name=article.candidate)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	try:
		source = Source.objects.get(name=article.source)
	except Source.DoesNotExist:
		raise Http404("Source does not exist")
	score=article.sentiment_score
	print(source.URL_logo)

	context={
		"article": article,
		"source": source,
		"candidate": candidate_id,
		"score": score
	}
	return render(request, 'badpress/article.html', context)


def about(request):
	return render(
		request,
		'badpress/about.html',
	)

def not_found_state(request):
	return render(request,'badpress/notfoundstate.html', {})

def tutorial(request):
	return render(request,'badpress/tutorial.html', {})

def error_404(request):
	return render(request,'badpress/404.html', {})

def error_500(request):
	return render(request,'badpress/404.html', {})
