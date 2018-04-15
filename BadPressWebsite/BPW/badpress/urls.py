from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('stateresults/', views.stateresults, name='stateresults'),
    path('candidate/', views.candidate, name='candidate'),
    path('article/', views.article, name='article'),
    path('issue/', views.issue, name='issue'),

    #url(r'^$', views.index, name="index"),
    #url(r'stateresults', views.stateresults, name="stateresults"),
    #url(r'candidate', views.candidate, name="candidate"),
    #url(r'article', views.article, name="article"),
    #url(r'issue',views.issue, name="issue"),
    #url(r'about', views.about, name="about")
]

