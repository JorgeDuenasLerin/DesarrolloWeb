from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo de los APIs.")

# Create your views here.
def nuevo(request):
    return HttpResponse("Hola mundo!")
