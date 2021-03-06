from django.conf.urls.defaults import *

urlpatterns = patterns('ultimate.junta.views',
	(r'^$', 'index', {}, 'junta'),

	(r'^captainstatus/$', 'captainstatus', {}, 'captainstatus'),
	(r'^captainstatus/(?P<year>\d{4})/(?P<season>[^/]+)/(?P<division>[^/]+)/$', 'captainstatus', {}, 'captainstatus_league'),

	(r'^leagueresults/$', 'leagueresults', {}, 'leagueresults'),
	(r'^leagueresults/(?P<year>\d{4})/(?P<season>[^/]+)/(?P<division>[^/]+)/$', 'leagueresults', {}, 'leagueresults_league'),

	(r'^registrationexport/$', 'registrationexport', {}, 'registrationexport'),
	(r'^registrationexport/(?P<year>\d{4})/(?P<season>[^/]+)/(?P<division>[^/]+)/$', 'registrationexport', {}, 'registrationexport_league'),

	(r'^teamimport/$', 'teamimport', {}, 'teamimport'),

	(r'^schedulegeneration/$', 'schedulegeneration', {}, 'schedulegeneration'),
	(r'^schedulegeneration/(?P<year>\d{4})/(?P<season>[^/]+)/(?P<division>[^/]+)/$', 'schedulegeneration', {}, 'schedulegeneration_league'),
)