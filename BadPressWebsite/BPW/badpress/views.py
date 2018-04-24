from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Source, State, Issue, Article, Candidate

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


def candidate(request, last_name):
	try:
		candidate_id=Candidate.objects.get(last_name=last_name)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	state="Texas"
	state_image="https://cdn.shopify.com/s/files/1/0394/9549/products/bigstock-Texas-Map-6029040.jpg?v=1496166825"
	#number_candidates=len(candidates)
	number_candidates=Candidate.objects.count()  # The 'all()' is implied by default.
	date="6th May 2018"
	#State.objects.filter(name__icontains="Texas")
	args={'candidate':candidate_id,'state': state, state_image : state_image,
	 "number_candidates": number_candidates, "date":date}
	return render(request, 'badpress/candidate.html', args)


def issue(request, id):
	try:
		candidate_id=Candidate.objects.get(id=id)
	except Candidate.DoesNotExist:
		raise Http404("Candidate does not exist")

	try:
		candidate_article = Article.objects.filter(candidate=id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	try:
		candidate_issue = Issue.objects.get(id=id)
	except Issue.DoesNotExist:
		raise Http404("Issue does not exist")

	try:
		candidate_source = Source.objects.get(id=id)
	except Source.DoesNotExist:
		raise Http404("Source does not exist")

	number=len(candidate_article)
	args={	"articles": candidate_article,
			"issue": candidate_issue,
			"source": candidate_source,
			"candidate": candidate_id,
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

