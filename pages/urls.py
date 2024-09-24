from django.urls import path

from pages.views import HomeView, aboutView, contactView, cartView 

urlpatterns = [
     path('home/', HomeView.as_view()),
     path('about/', aboutView),
     path('contact/', contactView),
     path('cart/', cartView),
]
