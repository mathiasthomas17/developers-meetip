from django.urls import path

# Import Views
from . import views

urlpatterns = [
    path('', views.projects,name = 'projects'),
    path('project/<str:pk>', views.project,name = 'project')
]