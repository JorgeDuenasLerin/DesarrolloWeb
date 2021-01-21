from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo del desarrollo django.")

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets
from rest_framework import permissions

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    #permission_classes = [permissions.IsAuthenticated]
