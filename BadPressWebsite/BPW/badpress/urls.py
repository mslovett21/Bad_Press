from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^stateresults/(?P<slug>[-\w]+)/$', views.state, name="state"),
    url(r'^candidate/(?P<last_name>\w+)/$', views.candidate, name="candidate"),
    url(r'^article/(?P<id>\d+)/$', views.article, name="article"),
    url(r'^issue/(?P<id>(\d))/(?P<last_name>(\w+))/$',views.issue, name="issue"),
    url(r'about', views.about, name="about")
]

