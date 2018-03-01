from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^main$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.regis),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^profile/(?P<id>\d+)$', views.profile),
    url(r'^addfriends$', views.addfriends),
    url(r'^addfriends/request/(?P<id>\d+)/$', views.requestfriends),
    url(r'^acceptfriends/(?P<id>\d+)/$', views.acceptfriends),
    url(r'^denyfriends/(?P<id>\d+)$', views.denyfriends),
    url(r'^unfriend/(?P<id>\d+)/$', views.unfriend),
    url(r'^creategroup$', views.creategroup),
    url(r'^group/(?P<id>\d+)$', views.group),
    url(r'^group/(?P<id>\d+)/results$', views.results),
    # url(r'^group/create$', views.groupcreate),
    # url(r'^group/create/submit$', views.groupsubmit),
    # url(r'^group/leave/(?P<id>\d+)$', views.groupleave),
    # url(r'^delete/(?P<id>\d+)$', views.delete),
]