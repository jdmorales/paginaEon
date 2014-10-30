from django.conf.urls import *
from django.template import loader, Context
from webPage.views import index

urlpatterns = patterns('',
    (r'^$', index.as_view()),
)

