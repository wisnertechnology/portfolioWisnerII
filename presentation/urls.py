from django.contrib import admin
from django.urls import path

from presentation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='hm'),
    path('contact/', views.contact, name='ct'),
    path('projects/', views.projects, name='pj'),
    path('resume/', views.resume, name='rs'),
    path('extractForm/', views.extractForm, name='exform'),
]
