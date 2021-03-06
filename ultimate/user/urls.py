from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = patterns('ultimate.user.views',
	(r'^$', 'index', {}, 'user'),

	(r'^login/$', login, {'template_name': 'user/login.html'}, 'auth_login'),
	(r'^logout/$', logout, {'template_name': 'user/logout.html'}, 'auth_logout'),

	(r'^password/reset/$', password_reset, {'post_reset_redirect': '/user/password/reset/done/', 'template_name': 'user/registration/password_reset_form.html', 'email_template_name': 'user/registration/password_reset_email.html', 'subject_template_name': 'user/registration/password_reset_subject.txt', }, 'password_reset'),
	(r'^password/reset/done/$', password_reset_done, {'template_name': 'user/registration/password_reset_done.html'}, 'password_reset_done'),
	(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': '/user/password/done/', 'template_name': 'user/registration/password_reset_confirm.html'}, 'password_reset_confirm'),
	(r'^password/done/$', password_reset_complete, {'template_name': 'user/registration/password_reset_complete.html'}, 'password_reset_confirm'),

	(r'^signup/$', 'signup', {}, 'registration_register'),
	(r'^editprofile/$', 'editprofile', {}, 'editprofile'),
	(r'^editskills/$', 'editskills', {}, 'editskills'),
)