from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'stateresults', views.stateresults, name="stateresults"),
    url(r'candidate', views.candidate, name="candidate"),
    url(r'article', views.article, name="article"),
    url(r'issue',views.issue, name="issue"),
    url(r'about', views.about, name="about"),
]

#url('/statetemplate', ListView.as_view(queryset=state.objects.all(), template_name="state/state.html")),