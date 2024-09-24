from django.http import HttpResponse 
from django.views.generic import TemplateView

# Create your views here.

# def homeView(request):
#     msg = 'hello world!'

#     return HttpResponse(msg) # returing and httpresponse object

# def aboutView(request):
#     msg = 'this is the about page'

#     return HttpResponse(msg) 

def contactView(requeat):
    msg = 'this is the contact page'

    return  HttpResponse(msg)

def cartView(requeat):
    msg = 'this is the cart page'

    return  HttpResponse(msg)

class HomeView(TemplateView):
    template = 'index.html'

def aboutView(request):

    msg = 'this is the about section of the website'


    return  HttpResponse(msg)