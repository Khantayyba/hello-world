from django.http import HttpResponse 
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# def homeView(request):
#     msg = 'hello world!'

#     return HttpResponse(msg) # returing and httpresponse object

# def aboutView(request):
#     msg = 'this is the about page'

#     return HttpResponse(msg) 


def cartView(requeat):
    msg = 'this is the cart page'

    return  HttpResponse(msg)

class HomeView(TemplateView):
    template_name = 'index.html'

# class AboutView(TemplateView):
#     template_name = 'about.html'

class ContactView(TemplateView): #P
    template_name = 'contact.html' #SNAKE CASE


def aboutView(request):
    return render(request, 'about.html')