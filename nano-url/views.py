# Create your views here.
#import django.contrib.staticfiles

from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

import os, random
from google.appengine.ext import db
from google.appengine.api import users


class Url(db.Model):
    input_url = db.StringProperty()
    string = db.StringProperty()
    appended_url = db.StringProperty()
    
def index(request):
    return render_to_response('index2.html', context_instance = RequestContext(request))

def detail(request):
    ip_url=request.POST['url']
    s = db.GqlQuery("SELECT * FROM Url WHERE  input_url = :1",ip_url)
    count = s.fetch(1)
    if count:
        appended_url = count[0].appended_url
        word = count[0].string
        return render_to_response('index2.html', {'appended_url':appended_url, 'word':word, 'show_url':True}, context_instance = RequestContext(request))
        
    else:
        char_array = "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
        word = "".join(random.choice(char_array) for i in range(4))
        appended_url = 'http://nano-url.appspot.com/'+word
        p=Url(input_url = ip_url, string = word, appended_url = appended_url )
        p.put()
        return render_to_response('index2.html', {'appended_url':appended_url, 'word':word, 'show_url':True}, context_instance = RequestContext(request))


def redirect(request,p):
    s = db.GqlQuery("SELECT * FROM Url WHERE  string = :1",p)
    count = s.fetch(1)
    url = count[0].input_url
    return HttpResponsePermanentRedirect(url)
 
