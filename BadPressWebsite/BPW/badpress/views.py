from django.shortcuts import render, HttpResponse, Http404
from django.views import generic
from .models import Source, State, Issue, Article, Candidate, Popularity, Cloud

# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Render the HTML template index.html with the data in the context variable
	queryset = Candidate.objects.all()
	context = {
		"candidate_list": queryset,
	}
	return render(
		request,
		'badpress/home.html',
		context
	)


class CandidateList(generic.ListView):
	model = Candidate
	state="Texas"
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['state_names'] = State.objects.all()
		return context

def state(request, slug):
	try:
		state_name=State.objects.get(name=slug)
	except State.DoesNotExist:
		raise Http404("State does not exist")

	try:
		candidates=Candidate.objects.filter(state=state_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	args={'candidates': candidates, 'state': state_name,}
	return render(request, 'badpress/candidate_list.html', args)

def candidate(request, last_name):
	try:
		candidate=Candidate.objects.get(last_name=last_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	candidate_id=candidate.id
	state=candidate.state
	popularity= Popularity.objects.get(id=candidate_id)
	cloud = Cloud.objects.get(id=candidate_id)
	print(state)
	print(popularity.october)
	print(cloud.word_1)
	state_image="https://cdn.shopify.com/s/files/1/0394/9549/products/bigstock-Texas-Map-6029040.jpg?v=1496166825"
	#number_candidates=len(candidates)
	number_candidates=Candidate.objects.count()  # The 'all()' is implied by default.
	date="6th May 2018"
	#State.objects.filter(name__icontains="Texas")
	args={'candidate':candidate,'state': state, 'state_image' : state_image, "popularity": popularity,
	 "number_candidates": number_candidates, "date":date, 'cloud' : cloud}
	return render(request, 'badpress/candidate.html', args)


def issue(request, id, last_name):
	try:
		candidate=Candidate.objects.get(last_name=last_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	try:
		candidate_id=candidate.id
		article = Article.objects.filter(candidate=candidate_id).filter(issue=id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	try:
		issue = Issue.objects.get(id=id)
	except Issue.DoesNotExist:
		raise Http404("Issue does not exist")

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
		article = Article.objects.get(id=id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	try:
		candidate_id=Candidate.objects.get(name=article.candidate)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")
	print(candidate_id)
	try:
		source = Source.objects.get(name=article.source)
	except Source.DoesNotExist:
		raise Http404("Source does not exist")

	context={
		"article": article,
		"source": source,
		"candidate": candidate_id,
	}
	return render(request, 'badpress/article.html', context)


def about(request):
	return render(
		request,
		'badpress/about.html',
	)

