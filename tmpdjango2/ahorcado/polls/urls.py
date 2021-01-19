from django.urls import path

from . import views

urlpatterns = [
    path('algomas/', views.index, name='index'),
]
