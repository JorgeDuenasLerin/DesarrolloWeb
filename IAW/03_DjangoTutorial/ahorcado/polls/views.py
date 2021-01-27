from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    preguntas = Question.objects.all()
    """
    Tarea/Reto
    1º Saca esta información como si fuera una lista HTML (ol-li)
    2º Saca de cada pregunta sus opciones
    """
    html = "<h1>Hola mundo del desarrollo django.</h1>"
    html = html + "<ol>"
    for p in preguntas:
        html = html + "<li>"
        html = html + p.question_text
        ## Quiero recorrer las opciones
        for o in p.choice_set.all():
            html = html + "<ul>"
            html = html + "<li>" + o.choice_text + "</li>"
            html = html + "</ul>"
        html = html + "</li>"
    html = html + "</ol>"
    return HttpResponse(html)


def detail(request, question_id):
    return HttpResponse("Este es el detalle de la pregunta con id: %s." % question_id)

def results(request, question_id):
    response = "Estás en el resultado de la pregunta con id %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Votación para " + str(question_id))
