from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),

    path('bugs/', views.bugs_view, name='bugs'),

    path('testcases/', views.testcases_view, name='testcases'),
]