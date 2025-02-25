from django.urls import path
from .import views

urlpatterns = [
    path("index/telesales/", views.telesales, name='telesales'),
]
