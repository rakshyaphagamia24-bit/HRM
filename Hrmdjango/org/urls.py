from django.urls import path
from . import views

urlpatterns = [
    path('', views.org_home, name='org_home'),
    path('units/', views.org_units, name='org_units'),
]