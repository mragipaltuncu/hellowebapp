from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import(
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    )


urlpatterns = patterns('',
	url(r'^$','collection.views.index',name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name="about.html"),
        name="about"),
    url(r'^contact/$',
        TemplateView.as_view(template_name="contact.html"),
        name="contact"),
    url(r'^things/(?P<slug>[-\w]+)$',
        'collection.views.thing_detail',
        name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$',
    'collection.views.edit_thing',
    name='edit_thing'),
    #Registration URLs
    url(r'^accounts/',
        include('registration.backends.simple.urls')),
    #Admin Site URLs
    url(r'^admin/', include(admin.site.urls)),
    #Password Reset URLs
    url(r'accounts/password/reset/$',
        password_reset,
        {'template_name':'registration/password_reset_form.html'},
        name='password_reset'),

    url(r'accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':'registration/password_reset_done.html'},
        name='password_reset_done'),

    url(r'accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name':'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),

    url(r'accounts/password/done/$',
        password_reset_complete,
        {'template_name':'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'accounts/$',include('registration.backends.default.urls')),

)
