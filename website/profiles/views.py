from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1> This is the profile for a candidate")