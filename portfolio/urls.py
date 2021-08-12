from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    
    path('', views.about, name='about'),
    path('hire/', views.hire, name='hire'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
