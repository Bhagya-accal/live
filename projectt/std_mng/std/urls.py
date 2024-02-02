from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('register/', views.register , name='register'),
    path('about/',views.about,name='about'),
    path('logout/',views.signout, name='signout'),
    path('view/<str:pk>/',views.view_details,name='details')
]
