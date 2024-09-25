from django.urls import path

from pages.views import HomeView, aboutView, ContactView, cartView 

urlpatterns = [
     path('', HomeView.as_view()), # class view/ methods attributes
     path('about/', aboutView, name='about'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('cart/', cartView),# function based view
]
