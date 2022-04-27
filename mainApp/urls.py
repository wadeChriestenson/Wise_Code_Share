from django.urls import path
from mainApp import views

urlpatterns = [
    path('', views.PostListView, name='Post View'),
]