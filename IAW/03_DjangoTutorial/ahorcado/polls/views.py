from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Question, Youtuber


def index(request):
    latest_question_list = Question.objects.all()
    context = {
        'listado_preguntas': latest_question_list,
        'titulo': 'Esta información va al template'
    }
    return render(request, 'polls/index.html', context)


def listado_youtubers(request):
    listado = Youtuber.objects.all()
    contexto = {
        'listado_youtubers': listado
    }
    return render(request, 'polls/listado_youtuber.html', contexto)


def detail(request, question_id):
    # Obterner la pregunta con id question_id a través de los modelos
    try:
        dondeGuardarElObjeto = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Lo que buscas no está")
    # Generar un contexto
    # generar un polls/detail.html
    # return -> return render
    context = {
        'pregunta': dondeGuardarElObjeto
    }
    return render(request, 'polls/detalle.html', context)


def results(request, question_id):
    response = "Estás en el resultado de la pregunta con id %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Votación para " + str(question_id))
