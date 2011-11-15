from django.conf.urls.defaults import *
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.index'),
    (r'^redirect$', 'views.detail'),
    (r'^(\w{4})$','views.redirect'),

)

