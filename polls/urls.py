from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
#WYSWIETLA MI STRONE PIERWSZA Z NAZWA QUIZU
    url(r'^$', views.IndexView.as_view(), name='index'),

#WYSWIETLA MI STRONE PIERWSZA Z NAZWA QUIZU
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#url(r'^([0-9]+)/([0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pytanie_id>[0-9]+)/vote/$', views.vote, name='vote'),
 #   url(r'^(?P<pytanie_id>\d+)/vote/$',views.vote, name='vote'),
]