from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1> This is the profile for a candidate")

def cadidate(request):
    template = loader.get_template('profiles/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

