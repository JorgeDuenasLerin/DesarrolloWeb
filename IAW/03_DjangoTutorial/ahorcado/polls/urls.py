from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('esto_es_lo_que_quieras', views.listado_youtubers, name = 'listado_youtubers'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/resultados/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/votar/', views.vote, name='vote'),


    path('primerjs/', TemplateView.as_view(template_name='polls/js1.html')),
]
