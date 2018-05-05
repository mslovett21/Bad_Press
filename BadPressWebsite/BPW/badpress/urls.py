from django.conf.urls import url, include
from django.urls import path
from . import views as badpress
from django.conf.urls import handler404, handler500

urlpatterns = [

    url(r'^$', badpress.index, name="index"),
    url(r'^stateresults/(?P<slug>[-\w]+)/$', badpress.state, name="state"),
    url(r'^candidate/(?P<last_name>\w+)/$', badpress.candidate, name="candidate"),
    url(r'^article/(?P<id>\d+)/$', badpress.article, name="article"),
    url(r'^issue/(?P<id>(\d))/(?P<last_name>(\w+))/$',badpress.issue, name="issue"),
    url(r'about', badpress.about, name="about"),
    url(r'state-not-found', badpress.not_found_state, name="not_found_state"),
    url(r'tutorial', badpress.tutorial, name="tutorial")
]

handler404 = badpress.error_404
handler500 = badpress.error_500

