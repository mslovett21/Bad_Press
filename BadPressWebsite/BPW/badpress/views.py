from django.shortcuts import render, HttpResponse
from .models import State
from django.views import generic
from .models import Source, State, Issue, Article, Candidate

# Create your views here.
# hello pushing this stuff
#def index(request):
#	return render(request, 'badpress/home.html')

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'badpress/home.html',
    )


def stateresults(request):
	state="Texas"
	candidates=[{"name":"Candidate 1", "party": "Republican"},{"name":"Candidate 2", "party": "Democrat"},
	{"name":"Candidate 3", "party": "Other"}, {"name":"Candidate 4", "party": "Democrat"},
	{"name":"Candidate 5", "party": "Republican"},{"name":"Candidate 6", "party": "Republican"},
	{"name":"Candidate 7", "party": "Democrat"}]
	state_image="https://cdn.shopify.com/s/files/1/0394/9549/products/bigstock-Texas-Map-6029040.jpg?v=1496166825"
	number_candidates=len(candidates)
	date="6th May 2018"
	args={'state': state, 'candidates': candidates, state_image : state_image,
	 "number_candidates": number_candidates, "date":date}
	return render(request, 'badpress/stateresults.html',args)


def candidate(request):
	return render(request, 'badpress/candidate.html')


def issue(request):
	candidate={"name" :"Ted Cruz"}
	issue={"name":"Gun Law", "info":"Gun laws in the United States regulate the sale, possession, and use of firearms and ammunition. State laws (and the laws of Washington, D.C. and the U.S. territories) vary considerably, and are independent of existing federal firearms laws, although they are sometimes broader or more limited in scope than the federal laws. State level laws vary significantly in their form, content, and level of restriction. Forty-four states have a provision in their state constitutions similar to the Second Amendment to the U.S. Constitution, which protects the right to keep and bear arms. The exceptions are California, Iowa, Maryland, Minnesota, New Jersey, and New York. In New York, however, the statutory civil rights laws contain a provision virtually identical to the Second Amendment. Additionally, the U.S. Supreme Court held in McDonald v. Chicago that the protections of the Second Amendment to keep and bear arms for self-defense in one's home apply against state governments and their political subdivisions.",
	"URL_logo":"https://cdn.cltampa.com/files/base/scomm/cltampa/image/2018/03/640w/gun_law.5aa311dbc246a.jpg"}
	articles=[{"newspaper": "CNN", "title": "Title1", "date": "02/07/2018"}, {"newspaper": "FoxNews", "title": "Title2", "date": "02/07/2018"},
	{"newspaper": "New York Times", "title": "Title3", "date": "02/07/2018"},{"newspaper": "CNN", "title": "Title4", "date": "02/07/2018"}]
	number=len(articles)
	args={"articles": articles, "issue":issue, "candidate": candidate, "number": number}
	return render(request, 'badpress/issue.html',args)



def article(request):
	return render(request, 'badpress/article.html')


'''
def about(request):
	return render(request, 'badpress/about.html')
'''

def about(request):
	return render(
        request,
        'badpress/about.html',
    )

