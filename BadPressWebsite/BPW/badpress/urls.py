from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
    #path('stateresults/', views.CandidateList.as_view(), name='stateresults'),
    #path('candidate/', views.candidate, name='candidate'),
    #path('candidate/<int:pk>', views.CandidateDetailView.as_view(), name='candidate-detail'),
    #url(r'profile/(?P<username>.+)/$', accountsViews.profile, name="profile")
    #path('article/', views.article, name='article'),
    #path('issue/', views.issue, name='issue'),

    url(r'^$', views.index, name="index"),
    url(r'^stateresults/(?P<slug>[-\w]+)/$', views.state, name="state"),
    url(r'^candidate/(?P<id>\d+)/$', views.candidate, name="candidate"),
    url(r'^article/(?P<id>\d+)/$', views.article, name="article"),
    url(r'^issue/(?P<id>\d+)/$',views.issue, name="issue"),
    url(r'about', views.about, name="about")
]

