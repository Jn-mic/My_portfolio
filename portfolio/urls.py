from django.urls import path

from . import views

urlpatterns=[
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('hire/', views.Hire, name='hire'),
    path('project/', views.Project, name='project'),
    path('contact/', views.Contact, name='contact'),
]