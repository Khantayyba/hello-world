
from django.contrib import admin
from django.urls import path

from pages.views import homeView, aboutView, contactView, cartView # importing the homeView function from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('about/', aboutView),
    path('contact/', contactView),
    path('cart/', cartView),
]

