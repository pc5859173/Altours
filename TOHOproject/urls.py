"""
Definition of urls for TOHOproject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms,views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('family/', views.family, name='family'),
    path('holiday/', views.holiday, name='holiday'),
    path('honeymoon/', views.honeymoon, name='honeymoon'),
    path('hotels/', views.hotels, name='hotels'),  
    path('amritsar/', views.amritsar, name='amritsar'),
    path('odisha/', views.odisha, name='odisha'), 
    path('gangtok/', views.gangtok, name='gangtok'),  
    path('jaipur/', views.jaipur, name='jaipur'),  
    path('kashmir/', views.kashmir, name='kashmir'),  
    path('hampi/', views.hampi, name='hampi'),  
    path('shimla/', views.shimla, name='shimla'), 
    path('mathura/', views.mathura, name='mathura'), 
    path('lehladakh/', views.lehladakh, name='lehladakh'),
    path('MadhyaPradesh/', views.MadhyaPradesh, name='MadhyaPradesh'),
    path('about/', views.about, name='about'),
    path('SaveData/', views.SaveData, name='SaveData'),
    path('goa/', views.goa, name='goa'),
    path('goahotels/', views.goahotels, name='goahotels'),
    path('hotelbooking/', views.hotelbooking, name='hotelbooking'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
