from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

    path('weather', views.weather, name='weather'),
    path('search',views.search,name='search'),


]